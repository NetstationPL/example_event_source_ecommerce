import re
from abc import ABC
from contextlib import contextmanager
from typing import Type
from uuid import UUID

from infra.event_store import EventStore
from infra.event_store.event_store import Event


class AggregateRoot(ABC):
    def __init__(self, uid: UUID) -> None:
        self.uid = uid
        self.unpublished_events = []

    def stream_name(self) -> str:
        return f"{self.__class__.__name__}#{self.uid}"

    def apply(self, event: Event) -> None:
        self._invoke_event_method(event)
        self.unpublished_events.append(event)

    def _invoke_event_method(self, event: Event) -> None:
        event_name = self._to_snake(event.__class__.__name__)
        method_name = f"apply_{event_name}"
        self.__getattribute__(method_name)(event)

    def _to_snake(self, text: str) -> str:
        return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()


class AggregateRootRepository:
    def __init__(self, event_store: EventStore) -> None:
        self.event_store = event_store

    @contextmanager
    def with_aggregate(self, aggregate: Type[AggregateRoot], uid: UUID):
        obj = aggregate(uid)
        yield obj
        for event in obj.unpublished_events:
            self.event_store.publish(event, obj.stream_name(uid))

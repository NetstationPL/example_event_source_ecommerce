import json
from decimal import Decimal
from typing import Callable, List, Type
from uuid import UUID

from infra.repository import Repository


def default(o):
    if isinstance(o, Decimal):
        return float(o)
    if isinstance(o, UUID):
        return str(o)
    return o.__dict__


class Event:
    def to_json(self):
        data = self.__dict__
        return json.dumps(data, sort_keys=True, indent=2, default=default)


class EventStore:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository
        self.subscriptions = []

    def publish(self, event: Event, stream_name: str = "GLOBAL") -> None:
        self.repository.save(event, stream_name)

        for handler, event_type in self.subscriptions:
            if isinstance(event, event_type):
                handler(event)

    def subscribe(
        self, handler: Callable[[Event], None], event_type: Type[Event]
    ) -> None:
        self.subscriptions.append((handler, event_type))

    def read_stream(self, stream_name: str) -> List[Event]:
        return self.repository.read(stream_name)

    def clear(self) -> None:
        self.repository.clear()  # pragma: no cover

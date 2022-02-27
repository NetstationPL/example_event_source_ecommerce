from typing import Callable, List
from infra.event_store import Event, EventStore
from infra.repository import Repository


class CQRS:
    def __init__(self, event_store: EventStore) -> None:
        self.event_store = event_store

    def publish(self, event: Event, stream_name: str) -> None:
        self.event_store.publish(event, stream_name)

    def subscribe(self, handler: Callable[[Event], None], event: Event) -> None:
        self.event_store.subscribe(handler, event)

    def all_events_from_stream(self, stream_name: str) -> List[Event]:
        return self.event_store.read_stream(stream_name)


cqrs = CQRS(EventStore(Repository()))

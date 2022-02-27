from infra.event_store import Event, EventStore
from infra.repository import Repository


class CQRS:
    def __init__(self, event_store):
        self.event_store = event_store

    def publish(self, event: Event):
        self.event_store.publish(event)

    def subscribe(self, handler, event):
        self.event_store.subscribe(handler, event)


cqrs = CQRS(EventStore(Repository()))

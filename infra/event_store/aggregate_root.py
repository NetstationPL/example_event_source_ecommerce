from contextlib import contextmanager

from infra.event_store import EventStore


class AggregateRootRepository:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    @contextmanager
    def with_aggregate(self, aggregate, uid):
        obj = aggregate(uid)
        yield obj
        for event in obj.unpublished_events:
            self.event_store.publish(event, obj.stream_name(uid))

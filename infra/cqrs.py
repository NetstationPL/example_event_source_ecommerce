from infra.event_store import Event


class CQRS:
    def __init__(self, event_store):
        self.event_store = event_store

    def publish(self, event: Event):
        self.event_store.publish(event)

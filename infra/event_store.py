class Event:
    pass


class EventStore:
    def __init__(self, repository):
        self.repository = repository
        self.subscriptions = []

    def publish(self, event: Event):
        self.repository.save(event)

        for handler, event_type in self.subscriptions:
            if isinstance(event, event_type):
                handler(event)

    def subscribe(self, handler, event_type):
        self.subscriptions.append((handler, event_type))

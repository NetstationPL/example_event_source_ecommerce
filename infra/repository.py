import logging
from infra.event_store import Event


class Repository:
    events = []

    def save(self, event: Event):
        logging.info(f"Saving event {event}")
        self.events.append(event)

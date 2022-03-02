import logging
from collections import defaultdict


class Repository:
    events: dict = defaultdict(list)

    def save(self, event, stream_name: str):
        logging.info(f"Saving event {event}")
        self.events[stream_name].append(event)

    def read(self, stream_name: str):
        logging.info(f"Reading stream {stream_name}")
        return self.events[stream_name]

    def clear(self):
        self.events.clear()

import logging


class Repository:
    events = []

    def save(self, event, stream_name: str):
        logging.info(f"Saving event {event}")
        self.events.append(event)

    def read(self, stream_name: str):
        logging.info(f"Reading stream {stream_name}")
        return self.events

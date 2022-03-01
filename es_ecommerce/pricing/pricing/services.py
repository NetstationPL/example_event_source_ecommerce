from infra.command_bus import Command
from infra.event_store import EventStore


class SetPriceHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    def handle(self, command: Command):
        pass

__version__ = "0.1.0"

from taxes.commands import SetVatRate

from infra import command_bus


class SetVatRateHandler:
    def __init__(self, event_store):
        self.event_store = event_store

    def handle(self, command):
        pass


def configure(cqrs):
    command_bus.register(SetVatRate, SetVatRateHandler(cqrs.event_store))

__version__ = "0.1.0"

from taxes.commands import SetVatRate
from taxes.services import SetVatRateHandler

from infra import command_bus


def configure(cqrs):
    command_bus.register(SetVatRate, SetVatRateHandler(cqrs.event_store))

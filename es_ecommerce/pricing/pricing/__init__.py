__version__ = "0.1.0"

from pricing.commands import SetPrice
from pricing.services import SetPriceHandler

from infra import command_bus


def configure(cqrs):
    command_bus.register(SetPrice, SetPriceHandler(cqrs.event_store))

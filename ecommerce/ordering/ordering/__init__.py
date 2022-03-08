from infra import command_bus

from .commands import AddItemToBasket
from .handlers import AddItemToBasketHandler


def configure(cqrs):
    command_bus.register(AddItemToBasket, AddItemToBasketHandler(cqrs.event_store))

from infra import command_bus

from .commands import AddItemToBasket, RemoveItemFromBasket
from .handlers import AddItemToBasketHandler, RemoveItemFromBasketHandler


def configure(cqrs):
    command_bus.register(AddItemToBasket, AddItemToBasketHandler(cqrs.event_store))
    command_bus.register(
        RemoveItemFromBasket, RemoveItemFromBasketHandler(cqrs.event_store)
    )

from infra.event_store import EventStore

from .commands import AddItemToBasket


class AddItemToBasketHandler:
    def __init__(self, event_store: EventStore) -> None:
        pass

    def handle(self, command: AddItemToBasket) -> None:
        pass

from typing import cast

from infra.event_store import EventStore
from infra.event_store.aggregate_root import AggregateRootRepository

from .commands import AddItemToBasket
from .order import Order


class AddItemToBasketHandler:
    def __init__(self, event_store: EventStore) -> None:
        self.event_store = event_store
        self.repository = AggregateRootRepository(event_store)

    def handle(self, command: AddItemToBasket) -> None:
        with self.repository.with_aggregate(Order, command.order_id) as order:
            cast(Order, order).add_item(command.product_id)

from typing import cast

from pricing.product import Product

from infra.event_store import EventStore
from infra.event_store.aggregate_root import AggregateRootRepository


class SetPriceHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store
        self.repository = AggregateRootRepository(event_store)

    def handle(self, command) -> None:
        with self.repository.with_aggregate(Product, command.product_id) as product:
            cast(Product, product).set_price(command.price)

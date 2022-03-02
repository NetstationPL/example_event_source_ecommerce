from infra.event_store.aggregate_root import AggregateRootRepository
from infra.event_store import EventStore

from pricing.product import Product


class SetPriceHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store
        self.repository = AggregateRootRepository(event_store)

    def handle(self, command) -> None:
        with self.repository.with_aggregate(Product, command.product_id) as product:
            product.set_price(command.price)

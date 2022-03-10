from pricing.events import PriceSet

from infra.event_store.aggregate_root import AggregateRoot
from infra.types import Money


class Product(AggregateRoot):
    price: Money

    def set_price(self, price: Money) -> None:
        event = PriceSet(self.uid, price=price)
        self.apply(event)

    def apply_price_set(self, event: PriceSet) -> None:
        self.price = event.price

    def stream_name(self) -> str:
        return f"Pricing#{self.uid}"

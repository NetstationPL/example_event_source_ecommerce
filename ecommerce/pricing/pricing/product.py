from pricing.events import PriceSet

from infra.event_store.aggregate_root import AggregateRoot


class Product(AggregateRoot):
    def set_price(self, price):
        event = PriceSet(self.uid, price=price)
        self.apply(event)

    def apply_price_set(self, event):
        self.price = event.price

    def stream_name(self, stream_name):
        return f"Pricing#{stream_name}"
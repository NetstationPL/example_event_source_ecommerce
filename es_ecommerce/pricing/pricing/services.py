from contextlib import contextmanager

from infra.event_store import EventStore

from pricing.events import PriceSet


class AggregateRootRepository:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    @contextmanager
    def with_aggregate(self, aggregate, uid):
        obj = aggregate(uid)
        yield obj
        for event in obj.unpublished_events:
            self.event_store.publish(event, obj.stream_name(uid))


class Product:
    def __init__(self, product_id):
        self.unpublished_events = []
        self.product_id = product_id

    def set_price(self, price):
        event = PriceSet(self.product_id, price=price)
        self.unpublished_events.append(event)

    def stream_name(self, stream_name):
        return f"Pricing#{stream_name}"


class SetPriceHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store
        self.repository = AggregateRootRepository(event_store)

    def handle(self, command) -> None:
        with self.repository.with_aggregate(Product, command.product_id) as product:
            product.set_price(command.price)

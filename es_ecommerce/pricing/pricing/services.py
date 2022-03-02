from infra.event_store import EventStore

from pricing.events import PriceSet


class SetPriceHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    def handle(self, command) -> None:
        self.event_store.publish(
            PriceSet(command.product_id, price=command.price),
            f"Pricing#{command.product_id}",
        )

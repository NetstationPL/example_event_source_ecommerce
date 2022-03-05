from typing import cast
from infra.event_store.aggregate_root import AggregateRootRepository

from infra.event_store.event_store import EventStore
import taxes.product


class SetVatRateHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store
        self.repository = AggregateRootRepository(event_store)

    def handle(self, command: "taxes.commands.SetVatRate"):
        with self.repository.with_aggregate(
            taxes.product.Product, command.product_id
        ) as product:
            cast(taxes.product.Product, product).set_vat_rate(command.vat_rate)

from taxes.events import VatRateSet

from infra.event_store.event_store import EventStore


class SetVatRateHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    def handle(self, command: "taxes.commands.SetVatRate"):
        self.event_store.publish(
            VatRateSet(product_id=command.product_id, vat_rate=command.vat_rate),
            f"Taxes#{command.product_id}",
        )

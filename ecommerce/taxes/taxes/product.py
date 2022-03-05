from taxes.events import VatRateSet
from infra.event_store.aggregate_root import AggregateRoot


class Product(AggregateRoot):
    def set_vat_rate(self, vat_rate):
        self.apply(VatRateSet(product_id=self.uid, vat_rate=vat_rate))

    def apply_vat_rate_set(self, event):
        self.vat_rate = event.vat_rate

    def stream_name(self, stream_name) -> str:
        return f"Taxes#{stream_name}"

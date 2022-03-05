from taxes import conf
from taxes.events import VatRateSet
from taxes.exceptions import VatRateNotApplicable

from infra.event_store.aggregate_root import AggregateRoot


class Product(AggregateRoot):
    def set_vat_rate(self, vat_rate):
        if not self.is_applicable(vat_rate):
            raise VatRateNotApplicable("Vat rate not applicable")
        self.apply(VatRateSet(product_id=self.uid, vat_rate=vat_rate))

    def apply_vat_rate_set(self, event):
        self.vat_rate = event.vat_rate

    def stream_name(self, stream_name) -> str:
        return f"Taxes#{stream_name}"

    def is_applicable(self, vat_rate):
        return vat_rate in conf.available_vat_rates

__version__ = "0.1.0"

from typing import List

from taxes.commands import SetVatRate

from infra import command_bus
from infra.types import VatRate


class Configuration:
    available_vat_rates: List[VatRate] = []

    def vat_rate_by_code(self, vat_code: str):
        return next(
            (vat for vat in self.available_vat_rates if vat.code == vat_code), None
        )


conf = Configuration()


def configure(cqrs, available_vat_rates):
    from taxes.services import SetVatRateHandler

    command_bus.register(SetVatRate, SetVatRateHandler(cqrs.event_store))
    conf.available_vat_rates = [
        VatRate(code=vat[1], rate=vat[0]) for vat in available_vat_rates
    ]

from unittest.mock import MagicMock
from uuid import uuid1

from taxes.commands import SetVatRate
from taxes.services import SetVatRateHandler
from taxes.taxes.events import VatRateSet

from infra.types import VatRate


def test_set_vat_rate_should_emit_event():
    event_store = MagicMock()

    uid = uuid1()
    command = SetVatRate(product_id=uid, vat_rate=VatRate("10", 10))

    SetVatRateHandler(event_store).handle(command)

    event_store.publish.assert_called_once_with(
        VatRateSet(product_id=uid, vat_rate=VatRate("10", 10)), f"Taxes#{uid}"
    )

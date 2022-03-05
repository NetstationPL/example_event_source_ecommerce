from decimal import Decimal
from unittest.mock import MagicMock
from uuid import uuid1

import pytest
from taxes import conf
from taxes.commands import SetVatRate
from taxes.events import VatRateSet
from taxes.exceptions import VatRateNotApplicable
from taxes.services import SetVatRateHandler

from infra.types import VatRate


def test_set_vat_rate_should_emit_event():
    event_store = MagicMock()
    conf.available_vat_rates = [VatRate("10", Decimal(10))]

    uid = uuid1()
    command = SetVatRate(product_id=uid, vat_rate=VatRate("10", Decimal(10)))

    SetVatRateHandler(event_store).handle(command)

    event_store.publish.assert_called_once_with(
        VatRateSet(product_id=uid, vat_rate=VatRate("10", Decimal(10))), f"Taxes#{uid}"
    )


def test_should_raise_exception_when_vat_rate_is_incorrect():
    event_store = MagicMock()
    conf.available_vat_rates = [VatRate("20", Decimal(20))]

    uid = uuid1()
    command = SetVatRate(product_id=uid, vat_rate=VatRate("10", Decimal(10)))

    with pytest.raises(VatRateNotApplicable):
        SetVatRateHandler(event_store).handle(command)

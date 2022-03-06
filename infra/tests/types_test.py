from decimal import Decimal

import pytest

from infra.types import Money, VatRate


def test_vat_rate_should_raise_exception_if_greater_than_100():
    with pytest.raises(ValueError):
        VatRate(code="101", rate=Decimal(101))


def test_vat_rate_should_raise_exception_if_less_than_0():
    with pytest.raises(ValueError):
        VatRate(code="-1", rate=Decimal(-1))


def test_money_should_raise_exception_if_less_than_0():
    with pytest.raises(ValueError):
        Money(-1)

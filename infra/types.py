from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class VatRate:
    code: str
    rate: Decimal

    def __post_init__(self) -> None:
        if self.rate < Decimal(0) or self.rate > Decimal("100.00"):
            raise ValueError(f"Vat rate must be between 0 and 100, got {self.rate}")


class Money(Decimal):
    pass

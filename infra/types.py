from dataclasses import dataclass
from decimal import Decimal


@dataclass
class VatRate:
    code: str
    rate: Decimal

from dataclasses import dataclass
from decimal import Decimal

from infra.event_store import Event


@dataclass
class PriceSet(Event):
    product_id: str
    price: Decimal

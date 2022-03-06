from dataclasses import dataclass
from uuid import UUID

from infra.event_store import Event
from infra.types import Money


@dataclass
class PriceSet(Event):
    product_id: UUID
    price: Money

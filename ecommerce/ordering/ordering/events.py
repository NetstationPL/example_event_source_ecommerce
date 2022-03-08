from dataclasses import dataclass
from uuid import UUID

from infra.event_store import Event


@dataclass
class ItemAddedToBasket(Event):
    order_id: UUID
    product_id: UUID


@dataclass
class ItemRemovedFromBasket(Event):
    order_id: UUID
    product_id: UUID

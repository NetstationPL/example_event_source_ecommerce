from dataclasses import dataclass
from uuid import UUID

from infra.event_store import Event


@dataclass
class ProductRegistered(Event):
    name: str
    product_id: UUID

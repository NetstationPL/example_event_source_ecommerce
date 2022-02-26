from dataclasses import dataclass
from uuid import UUID


@dataclass
class ProductRegistered:
    name: str
    product_id: UUID

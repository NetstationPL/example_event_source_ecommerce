from dataclasses import dataclass
from uuid import UUID


@dataclass
class RegisterProduct:
    product_id: UUID
    name: str

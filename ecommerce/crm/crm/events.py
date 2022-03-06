from dataclasses import dataclass
from uuid import UUID

from infra.event_store import Event


@dataclass
class CustomerRegistered(Event):
    customer_id: UUID
    name: str

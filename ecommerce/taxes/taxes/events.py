from dataclasses import dataclass
from uuid import UUID

from infra.event_store.event_store import Event
from infra.types import VatRate


@dataclass
class VatRateSet(Event):
    product_id: UUID
    vat_rate: VatRate

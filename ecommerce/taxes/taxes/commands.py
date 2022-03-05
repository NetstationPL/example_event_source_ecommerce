from dataclasses import dataclass
from uuid import UUID

from infra.command_bus import Command
from infra.types import VatRate


@dataclass
class SetVatRate(Command):
    product_id: UUID
    vat_rate: VatRate

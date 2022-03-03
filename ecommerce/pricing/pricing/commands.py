from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from infra.command_bus import Command


@dataclass
class SetPrice(Command):
    product_id: UUID
    price: Decimal

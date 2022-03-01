from dataclasses import dataclass
from uuid import UUID
from decimal import Decimal

from infra.command_bus import Command


@dataclass
class SetPrice(Command):
    product_id: UUID
    price: Decimal

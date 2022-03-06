from dataclasses import dataclass
from uuid import UUID

from infra.command_bus import Command
from infra.types import Money


@dataclass
class SetPrice(Command):
    product_id: UUID
    price: Money

from dataclasses import dataclass
from uuid import UUID

from infra.command_bus import Command


@dataclass
class AddItemToBasket(Command):
    order_id: UUID
    product_id: UUID

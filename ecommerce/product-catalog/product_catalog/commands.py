from dataclasses import dataclass
from uuid import UUID

from infra.command_bus import Command


@dataclass
class RegisterProduct(Command):
    product_id: UUID
    name: str

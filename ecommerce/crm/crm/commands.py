from dataclasses import dataclass
from uuid import UUID

from infra.command_bus import Command


@dataclass
class RegisterCustomer(Command):
    customer_id: UUID
    name: str

from dataclasses import dataclass

from infra.command_bus import Command


@dataclass
class SetVatRate(Command):
    pass

from infra.command_bus import Command, CommandHandler


class Registration(CommandHandler):
    def __init__(self, cqrs):
        self.cqrs = cqrs

    def handle(self, command: Command) -> None:
        print("Registration")

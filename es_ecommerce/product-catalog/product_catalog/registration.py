from infra.command_bus import Command, CommandHandler


class Registration(CommandHandler):
    def handle(self, command: Command) -> None:
        print("Registration")

class SetVatRateHandler:
    def __init__(self, event_store):
        self.event_store = event_store

    def handle(self, command: "taxes.commands.SetVatRate"):
        pass

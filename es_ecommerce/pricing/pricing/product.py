from pricing.events import PriceSet


class Product:
    def __init__(self, product_id):
        self.unpublished_events = []
        self.product_id = product_id

    def set_price(self, price):
        event = PriceSet(self.product_id, price=price)
        self.unpublished_events.append(event)

    def stream_name(self, stream_name):
        return f"Pricing#{stream_name}"

from django.apps import AppConfig
from ordering import configure
from ordering.events import ItemAddedToBasket, ItemRemovedFromBasket

from infra.cqrs import cqrs


class OrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "orders"

    def ready(self):
        from orders import handlers

        configure(cqrs)

        cqrs.subscribe(handlers.add_item_to_basket, ItemAddedToBasket)
        cqrs.subscribe(handlers.remove_item_from_basket, ItemRemovedFromBasket)

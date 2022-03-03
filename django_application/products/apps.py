import pricing
from django.apps import AppConfig
from infra.cqrs import cqrs

from pricing.events import PriceSet
from product_catalog import configure
from product_catalog.events import ProductRegistered

from products import handlers


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"

    def ready(self):
        from events.repository import DjangoRepository
        configure(cqrs)
        cqrs.set_repository(DjangoRepository())
        cqrs.subscribe(handlers.create_product, ProductRegistered)
        cqrs.subscribe(handlers.set_price, PriceSet)
        pricing.configure(cqrs)

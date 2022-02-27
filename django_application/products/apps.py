from django.apps import AppConfig
from product_catalog import configure
from product_catalog.events import ProductRegistered
from infra.cqrs import cqrs
from products import handlers


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"

    def ready(self):
        configure(cqrs)
        cqrs.subscribe(handlers.create_product, ProductRegistered)

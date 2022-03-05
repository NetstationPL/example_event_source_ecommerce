import pricing
import taxes
from django.apps import AppConfig
from django.conf import settings
from pricing.events import PriceSet
from product_catalog import configure
from product_catalog.events import ProductRegistered
from products import handlers

from infra.cqrs import cqrs


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"

    def ready(self):
        from infra.event_store.django_event_store.repository import \
            DjangoRepository

        configure(cqrs)
        cqrs.set_repository(DjangoRepository())
        cqrs.subscribe(handlers.create_product, ProductRegistered)
        cqrs.subscribe(handlers.set_price, PriceSet)
        pricing.configure(cqrs)
        taxes.configure(cqrs, settings.AVAILABLE_VAT_RATES)

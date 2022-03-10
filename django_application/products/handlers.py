from pricing.events import PriceSet
from product_catalog.events import ProductRegistered
from taxes.events import VatRateSet


def create_product(event: ProductRegistered) -> None:
    from products.models import Product

    product = Product(uid=event.product_id, name=event.name)
    product.save()


def set_price(event: PriceSet) -> None:
    from products.models import Product

    product = Product.objects.get(uid=event.product_id)
    product.price = event.price
    product.save()


def set_vat_rate(event: VatRateSet) -> None:
    from products.models import Product

    product = Product.objects.get(uid=event.product_id)
    product.vat_rate = event.vat_rate.rate
    product.save()

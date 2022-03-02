from product_catalog.events import ProductRegistered
from pricing.events import PriceSet


def create_product(event: ProductRegistered) -> None:
    from products.models import Product

    product = Product(id=event.product_id, name=event.name)
    product.save()


def set_price(event: PriceSet) -> None:
    from products.models import Product

    product = Product.objects.get(id=event.product_id)
    product.price = event.price
    product.save()

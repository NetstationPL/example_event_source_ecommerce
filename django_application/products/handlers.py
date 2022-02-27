from product_catalog.events import ProductRegistered


def create_product(event: ProductRegistered) -> None:
    from products.models import Product

    product = Product(id=event.product_id, name=event.name)
    product.save()

from ordering.events import ItemAddedToBasket
from products.models import Product

from .models import OrderLine


def add_item_to_basket(event: ItemAddedToBasket):
    product = Product.objects.get(id=event.product_id)
    ol, _ = OrderLine.objects.get_or_create(
        order_id=event.order_id,
        product_id=event.product_id,
        defaults={
            "quantity": 0,
            "price": product.price,
        },
    )

    ol.quantity += 1
    ol.save()


def remove_item_from_basket(event: ItemAddedToBasket):
    OrderLine.objects.filter(
        order_id=event.order_id, product_id=event.product_id
    ).delete()

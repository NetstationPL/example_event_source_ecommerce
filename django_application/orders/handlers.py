from ordering.events import ItemAddedToBasket
from products.models import Product

from .models import Order, OrderLine


def add_item_to_basket(event: ItemAddedToBasket):
    product = Product.objects.get(uid=event.product_id)
    order, _ = Order.objects.get_or_create(uid=event.order_id)
    ol, _ = OrderLine.objects.get_or_create(
        order=order,
        product_id=event.product_id,
        defaults={
            "quantity": 0,
            "price": product.price,
            "product_name": product.name,
        },
    )

    ol.quantity += 1
    ol.save()
    order.save()


def remove_item_from_basket(event: ItemAddedToBasket):
    ol = OrderLine.objects.filter(
        order__uid=event.order_id, product_id=event.product_id
    ).first()
    if ol and ol.quantity == 1:
        return ol.delete()
    ol.quantity -= 1
    ol.save()

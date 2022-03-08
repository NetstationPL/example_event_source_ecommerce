from django import template

register = template.Library()


@register.filter
def get_item(order_lines, product_id):
    return order_lines.filter(product_id=product_id).first()

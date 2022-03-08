from django import template

register = template.Library()


@register.filter
def money(value: str) -> str:
    return f"${value}" if value else ""

import json

from django.contrib import admin
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "stream", "json_pretty")

    def json_pretty(self, instance: Event):
        formatter = HtmlFormatter(style="colorful")
        response = highlight(instance.data, JsonLexer(), formatter)

        style = (
            "<style>" + formatter.get_style_defs() + "\npre { margin: 0px; }</style>"
        )

        return mark_safe(style + response)

    json_pretty.short_description = "data prettified"

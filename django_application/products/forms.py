import uuid

from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    product_id = forms.UUIDField(widget=forms.HiddenInput(), initial=uuid.uuid1)

    class Meta:
        model = Product
        fields = ("name", "price", "vat_rate")

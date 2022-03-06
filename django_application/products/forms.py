import uuid

from django import forms
from taxes import conf


class VatRateField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        choices = [(vat.code, vat.code) for vat in conf.available_vat_rates]
        choices.insert(0, ("", "---"))
        kwargs["choices"] = choices
        super().__init__(*args, **kwargs)


class ProductForm(forms.Form):
    product_id = forms.UUIDField(widget=forms.HiddenInput(), initial=uuid.uuid1)
    name = forms.CharField(label="Name", max_length=100)
    price = forms.DecimalField(label="Price", max_digits=10, decimal_places=2)
    vat_rate = VatRateField(label="VAT Rate", required=False)

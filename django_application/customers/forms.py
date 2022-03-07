import uuid

from django import forms


class CustomerForm(forms.Form):
    customer_id = forms.UUIDField(widget=forms.HiddenInput(), initial=uuid.uuid1)
    name = forms.CharField(label="Name", max_length=200)

from django import forms


class CustomerForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)

import django
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import generic
from pricing.commands import SetPrice
from product_catalog.commands import RegisterProduct
from product_catalog.exceptions import AlreadyRegistered
from taxes.commands import SetVatRate

from infra import command_bus

from .forms import ProductForm
from .models import Product


class IndexView(generic.ListView):
    template_name = "products/index.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all()


class DetailView(generic.DetailView):
    model = Product
    template_name = "products/detail.html"


class ProductFormView(generic.TemplateView):
    template_name = "products/new.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProductForm()
        return context

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            with django.db.transaction.atomic():
                try:
                    command_bus.call(
                        RegisterProduct(
                            product_id=form.cleaned_data["product_id"],
                            name=form.cleaned_data["name"],
                        )
                    )
                    if form.cleaned_data["price"]:
                        command_bus.call(
                            SetPrice(
                                product_id=form.cleaned_data["product_id"],
                                price=form.cleaned_data["price"],
                            )
                        )
                    if form.cleaned_data["vat_rate"]:
                        command_bus.call(
                            SetVatRate(
                                product_id=form.cleaned_data["product_id"],
                                vat_rate=form.cleaned_data["vat_rate"],
                            )
                        )
                except AlreadyRegistered:
                    messages.error(request, "Product was already registered")
                    return redirect("products:new")
            return redirect("products:index")
        messages.error(request, "Form is not valid")
        return render(request, "products/new.html", {"form": form})

from dataclasses import dataclass

from django.views import generic

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


class CommandBus:
    pass


@dataclass
class CreateProductCommand:
    name: str
    price: float
    vat_rate_code: int


class ProductCreateView(generic.View):
    command_bus = CommandBus()

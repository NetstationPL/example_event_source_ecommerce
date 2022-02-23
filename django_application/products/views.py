from django.shortcuts import redirect
from django.views import generic
from product_catalog.commands import RegisterProduct

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
    def notify(self, command):
        pass


class ProductCreateView(generic.View):
    command_bus = CommandBus()

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            self.command_bus.notify(
                RegisterProduct(
                    product_id=form.cleaned_data["product_id"],
                    name=form.cleaned_data["name"],
                )
            )
            return redirect("products:index")

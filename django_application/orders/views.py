import uuid

from customers.models import Customer
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from products.models import Product

from .models import Order


class OrdersListView(ListView):
    model = Order
    template_name = 'orders/index.html'
    context_object_name = 'orders'


class OrdersCreateView(TemplateView):
    template_name = "orders/new.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_id'] = uuid.uuid4()
        context['products'] = Product.objects.all()
        context['customers'] = Customer.objects.all()
        return context


class OrdersAddItemView(TemplateView):
    template_name = "orders/add_item.html"

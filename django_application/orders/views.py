import uuid

from customers.models import Customer
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import TemplateView, View
from products.models import Product

from infra import command_bus

from .models import Order, OrderLine


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


class OrdersAddItemView(View):
    def post(self, request, order_id: uuid.UUID):
        product_id = request.POST.get('product_id')

        return redirect(reverse("orders:edit", args=(order_id,)))


class OrdersEditView(TemplateView):
    template_name = "orders/edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_id = kwargs['order_id']
        context['order_id'] = order_id
        context['products'] = Product.objects.all()
        context['order_lines'] = OrderLine.objects.filter(order_id=order_id)
        context['customers'] = Customer.objects.all()
        return context


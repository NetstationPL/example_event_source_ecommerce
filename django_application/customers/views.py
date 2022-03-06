from crm.commands import RegisterCustomer
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from infra import command_bus

from .forms import CustomerForm
from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"


class CustomerCreateView(FormView):
    form_class = CustomerForm
    template_name = "customers/new.html"
    success_url = reverse_lazy("customers:index")

    def form_valid(self, form):
        command_bus.call(RegisterCustomer(**form.cleaned_data))
        return super().form_valid(form)

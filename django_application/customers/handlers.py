from crm.events import CustomerRegistered

from .models import Customer


def create_customer(event: CustomerRegistered):
    customer = Customer.objects.create(
        id=event.customer_id,
        name=event.name,
    )
    customer.save()

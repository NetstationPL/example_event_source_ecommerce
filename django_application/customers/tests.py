import uuid

from customers.models import Customer
from django.test import TestCase


class CustomersTestCase(TestCase):
    def test_customers_page(self):
        Customer.objects.create(name="John Smith")
        Customer.objects.create(name="Jane Doe")

        response = self.client.get("/customers/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Smith")
        self.assertContains(response, "Jane Doe")


class CustomerAddTestCase(TestCase):
    def setUp(self) -> None:
        Customer.objects.all().delete()

    def test_customer_add_page(self):
        response = self.client.get("/customers/new/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "customers/new.html")

    def test_customer_add(self):
        uid = uuid.uuid4()
        response = self.client.post(
            "/customers/new/",
            {
                "customer_id": uid,
                "name": "John Smith",
            },
            follow=True,
        )
        self.assertTemplateUsed(response, "customers/index.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Smith")

from customers.models import Customer
from django.test import TestCase


class CustomersTestCase(TestCase):
    def test_customers_page(self):
        Customer.objects.create(name='John Smith')
        Customer.objects.create(name='Jane Doe')

        response = self.client.get('/customers/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Smith')
        self.assertContains(response, 'Jane Doe')

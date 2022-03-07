from customers.models import Customer
from django.test import TestCase
from products.models import Product


class OrdersCreayeTest(TestCase):
    def test_order_new_page(self):
        Product.objects.create(name='Django', price=10)
        Product.objects.create(name='Flask', price=10)
        Customer.objects.create(name='John')

        response = self.client.get('/orders/new/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/new.html')
        self.assertContains(response, "Django")
        self.assertContains(response, "Flask")
        self.assertContains(response, "John")

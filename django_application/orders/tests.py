import uuid

from bs4 import BeautifulSoup
from customers.models import Customer
from django.test import TestCase
from products.models import Product


class OrdersCreayeTest(TestCase):
    def test_order_new_page(self):
        Product.objects.create(name="Django", price=10)
        Product.objects.create(name="Flask", price=10)
        Customer.objects.create(name="John")

        response = self.client.get("/orders/new/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/new.html")
        self.assertContains(response, "Django")
        self.assertContains(response, "Flask")
        self.assertContains(response, "John")

    def test_add_item_to_order(self):
        product = Product.objects.create(name="Django", price=10)
        order_id = uuid.uuid4()

        response = self.client.post(
            f"/orders/{ order_id }/add_item/",
            {
                "product_id": product.id,
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/edit.html")
        html = BeautifulSoup(response.content, "html.parser")
        row = html.find("td", text=product.name)
        cells = [cell.getText() for cell in row.parent.find_all("td")]

        self.assertEqual(cells[1], "1")
        self.assertEqual(cells[2], "$10")
        self.assertEqual(cells[3], "$10")
        self.assertEqual(cells[4], "Add")
        self.assertEqual(cells[5], "Remove")

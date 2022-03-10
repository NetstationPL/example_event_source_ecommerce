import uuid

from bs4 import BeautifulSoup
from customers.models import Customer
from django.test import TestCase
from products.models import Product

from .models import Order


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
                "product_id": product.uid,
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/edit.html")

        cells = self.get_row_with_product_name(response.content, product.name)
        self.assertEqual(cells[1], "1")
        self.assertEqual(cells[2], "$10.00")
        self.assertEqual(cells[3], "$10.00")
        self.assertEqual(cells[4].strip(), "Add")
        self.assertEqual(cells[5].strip(), "Remove")

    def test_remove_item_from_order(self):
        product = Product.objects.create(name="Django", price=10)
        order_id = uuid.uuid4()

        self.add_item_to_order(order_id, product.uid)

        response = self.client.post(
            f"/orders/{ order_id }/remove_item/",
            {
                "product_id": product.uid,
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/edit.html")

        cells = self.get_row_with_product_name(response.content, product.name)
        self.assertEqual(cells[1], "")
        self.assertEqual(cells[2], "")
        self.assertEqual(cells[3], "")
        self.assertEqual(cells[4].strip(), "Add")
        self.assertNotEqual(cells[5].strip(), "Remove")

    def test_remove_item_from_order_if_quantity_gt_1(self):
        order_id = uuid.uuid4()
        product = Product.objects.create(name="Django", price=10)
        self.add_item_to_order(order_id, product.uid)
        self.add_item_to_order(order_id, product.uid)

        response = self.client.post(
            f"/orders/{ order_id }/remove_item/",
            {
                "product_id": product.uid,
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/edit.html")

        cells = self.get_row_with_product_name(response.content, product.name)
        self.assertEqual(cells[1], "1")
        self.assertEqual(cells[2], "$10.00")
        self.assertEqual(cells[3], "$10.00")
        self.assertEqual(cells[4].strip(), "Add")
        self.assertEqual(cells[5].strip(), "Remove")

    def test_order_total(self):
        order_id = uuid.uuid4()
        product1 = Product.objects.create(name="Django", price=10)
        product2 = Product.objects.create(name="Django", price=20)

        self.add_item_to_order(order_id, product1.uid)
        response = self.add_item_to_order(order_id, product2.uid)

        self.assert_total_in_table(response.content, "$30.00")

    def assert_total_in_table(self, content, total):
        html = BeautifulSoup(content, "html.parser")
        total_cell = html.find("td", text="Total")
        self.assertIsNotNone(total_cell, "Table footer not found")
        self.assertEqual(total_cell.find_next_sibling("td").getText().strip(), total)

    def add_item_to_order(self, order_id, product_id):
        return self.client.post(
            f"/orders/{ order_id }/add_item/",
            {
                "product_id": product_id,
            },
            follow=True,
        )

    def get_row_with_product_name(self, content, name):
        html = BeautifulSoup(content, "html.parser")
        row = html.find("td", text=name)
        return [cell.getText() for cell in row.parent.find_all("td")]


class OrderViewTest(TestCase):
    def test_order_index_page(self):
        Order.objects.create(uid=uuid.uuid4())

        response = self.client.get("/orders/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/index.html")
        self.assertContains(response, "Not submited")
        self.assertContains(response, "Draft")

    def test_order_detail_page(self):
        order = Order.objects.create(uid=uuid.uuid4())
        product_uid = uuid.uuid4()
        order.orderline_set.create(
            product_id=product_uid, product_name="Django", quantity=1, price=10
        )
        Product.objects.create(name="Django", price=10)

        response = self.client.get(f"/orders/{ order.uid }/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/detail.html")
        self.assertContains(response, "Draft")
        self.assertContains(response, "Django")

from uuid import UUID

from django.test import TestCase
from products.models import Product

from infra.cqrs import cqrs


class TestProducts(TestCase):
    def tearDown(self) -> None:
        cqrs.clear_event_store()
        Product.objects.all().delete()
        return super().tearDown()

    def test_products_page(self):
        product1 = self._product_was_created()
        product2 = self._product_was_created()

        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/index.html")
        self.assertContains(response, "<h1>Products</h1>")
        self.assertContains(response, product1.name)
        self.assertContains(response, product2.name)

    def test_product_detail_page(self):
        product = self._product_was_created()
        response = self.client.get(f"/products/{product.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/detail.html")
        self.assertContains(response, f"<h1>{ product.name }</h1>")
        self.assertContains(response, product.price)
        self.assertContains(response, f"{ product.vat_rate_code }%")

    def test_product_detail_page_not_found(self):
        response = self.client.get(f"/products/ff0e9cde-8579-4af3-a078-7f8137b1bf9f/")
        self.assertEqual(response.status_code, 404)

    def test_product_detail_page_not_found_with_invalid_id(self):
        response = self.client.get("/products/aaaa/")
        self.assertEqual(response.status_code, 404)

    def test_product_create_page(self):
        response = self.client.get("/products/new/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/new.html")
        self.assertContains(response, "<h1>Create Product</h1>")

    def test_product_create_only_with_name(self):
        response = self.client.post(
            "/products/create/",
            {
                "product_id": "ff0e9cde-8579-4af3-a078-7f8137b1bf9f",
                "name": "Test Product 2",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "products/index.html")
        self.assertContains(response, "Test Product 2")

    def send_create_product(self, product_id: UUID):
        return self.client.post(
            "/products/create/",
            {
                "product_id": product_id,
                "name": "Test Product 2",
            },
            follow=True,
        )

    def test_product_already_registered(self):
        product_id = UUID("ff0e9cde-8579-4af3-a078-7f8137b1bf9f")
        self.send_create_product(product_id)
        response = self.send_create_product(product_id)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "products/new.html")
        self.assertContains(response, "Product was already registered")

    def _product_was_created(self):
        return Product.objects.create(
            name="Test Product 1", price=10.00, vat_rate_code=10
        )

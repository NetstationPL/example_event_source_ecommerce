from django.test import TestCase
from django.test.html import parse_html

from products.models import Product


class TestProducts(TestCase):
    def tearDown(self) -> None:
        Product.objects.all().delete()
        return super().tearDown()

    def test_products_page(self):
        Product.objects.create(name="Test Product 1", price=10.00, vat_rate_code=10)
        Product.objects.create(name="Test Product 2", price=20.00, vat_rate_code=20)

        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/index.html")
        self.assertContains(response, "<h1>Products</h1>")
        self.assertContains(response, "Test Product 1")
        self.assertContains(response, "Test Product 2")

    def test_product_detail_page(self):
        product = Product.objects.create(
            name="Test Product 1", price=10.00, vat_rate_code=10
        )
        response = self.client.get(f"/products/{product.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/detail.html")
        self.assertContains(response, "<h1>Test Product 1</h1>")
        self.assertContains(response, "10.00")
        self.assertContains(response, "10%")

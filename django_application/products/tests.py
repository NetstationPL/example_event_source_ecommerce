from django.test import TestCase

from products.models import Product


class TestProducts(TestCase):
    def setUp(self) -> None:
        Product.objects.create(name="Test Product 1", price=10.00, vat_rate_code=10)
        Product.objects.create(name="Test Product 2", price=20.00, vat_rate_code=20)
        return super().setUp()

    def test_products_page(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/index.html")
        self.assertContains(response, "Test Product 1")
        self.assertContains(response, "Test Product 2")

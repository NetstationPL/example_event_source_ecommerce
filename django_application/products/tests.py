from django.test import TestCase

from products.models import Product


class TestProducts(TestCase):
    def tearDown(self) -> None:
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

    def _product_was_created(self):
        return Product.objects.create(
            name="Test Product 1", price=10.00, vat_rate_code=10
        )


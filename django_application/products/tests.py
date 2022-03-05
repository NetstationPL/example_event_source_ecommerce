from uuid import UUID, uuid1

from bs4 import BeautifulSoup
from django.test import TestCase, override_settings
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
        self.assertContains(response, "Products")
        self.assertContains(response, product1.name)
        self.assertContains(response, product2.name)

    def test_product_detail_page(self):
        product = self._product_was_created()
        response = self.client.get(f"/products/{product.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/detail.html")
        self.assertContains(response, f"{ product.name }")

    def test_product_detail_page_not_found(self):
        response = self.client.get(f"/products/ff0e9cde-8579-4af3-a078-7f8137b1bf9f/")
        self.assertEqual(response.status_code, 404)

    def test_product_detail_page_not_found_with_invalid_id(self):
        response = self.client.get("/products/aaaa/")
        self.assertEqual(response.status_code, 404)

    @override_settings(AVAILABLE_VAT_RATES=[("10", 10)])
    def test_product_create_page(self):
        response = self.client.get("/products/new/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/new.html")
        self.assertContains(response, "Create Product")
        options = self.options_from_select("id_vat_rate", response)

        self.assertEqual(len(list(options)), 3)
        self.assertEqual(options[1].text, "10")

    def options_from_select(self, name, response):
        select = BeautifulSoup(response.content, "html.parser").find("select", id=name)
        if select:
            return select.find_all("option")
        return []

    def test_product_create_only_with_name(self):
        product_id = uuid1()
        response = self.send_create_product(product_id)
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "products/index.html")
        self.assertContains(response, "Test Product 2")

    def test_register_many_different_productsd(self):
        product1_id = uuid1()
        product2_id = uuid1()
        self.send_create_product(product1_id)
        response = self.send_create_product(product2_id)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "products/index.html")
        self.assertNotContains(response, "Product was already registered")

    def test_product_already_registered(self):
        product_id = UUID("ff0e9cde-8579-4af3-a078-7f8137b1bf9f")
        self.send_create_product(product_id)
        response = self.send_create_product(product_id)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "products/new.html")
        self.assertContains(response, "Product was already registered")

    def test_form_is_not_valid(self):
        product_id = UUID("ff0e9cde-8579-4af3-a078-7f8137b1bf9f")
        response = self.send_create_product(product_id, name="")

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "products/new.html")
        self.assertContains(response, "Form is not valid")

    def test_product_create_with_price(self):
        product_id = UUID("ff0e9cde-8579-4af3-a078-7f8137b1bf9f")
        response = self.send_create_product(product_id, price=12.34)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "products/index.html")
        self.assertContains(response, "$12.34")

    def test_product_create_with_vat_rate(self):
        product_id = UUID("ff0e9cde-8579-4af3-a078-7f8137b1bf9f")
        response = self.send_create_product(product_id, vat_rate="10")

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "products/index.html")
        txt = self.third_column_of("Test Product 2", response)
        self.assertEqual(txt, "10")

    def third_column_of(self, name, response):
        return (
            BeautifulSoup(response.content, "html.parser")
            .find("td", text=name)
            .find_next_sibling("td")
            .find_next_sibling("td")
            .text
        )

    def _product_was_created(self):
        return Product.objects.create(name="Test Product 1", price=10.00, vat_rate=10)

    def send_create_product(
        self, product_id: UUID, name="Test Product 2", price=10.00, vat_rate=""
    ):
        return self.client.post(
            "/products/new/",
            {
                "product_id": product_id,
                "name": name,
                "price": price,
                "vat_rate": vat_rate,
            },
            follow=True,
        )

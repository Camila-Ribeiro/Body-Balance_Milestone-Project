from django.test import TestCase
from products.models import Product


class TestViews(TestCase):

    def test_products_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)

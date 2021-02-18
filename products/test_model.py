from django.test import TestCase
from .models import Category


class TestModels(TestCase):

    def test_category(self):
        # category = Item.objects.create(name='Test Categories')
        self.assertFalse(category.done)

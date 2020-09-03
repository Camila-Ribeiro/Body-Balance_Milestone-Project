from django.db import models

# models


class Category(models.Model):

    category_friendly_name = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    def get_category_friendly_name(self):
        return self.category_friendly_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True, )
    sku = models.CharField(max_length=100)
    product_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024)
    image_file = models.ImageField()

    def __str__(self):
        return self.product_name

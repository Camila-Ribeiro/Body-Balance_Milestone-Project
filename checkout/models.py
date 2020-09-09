import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

# Create your models here.



class ProductOrder(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    shop_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def get_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update shopping bag total each time an order is added to the queue,
        accounting for delivery costs.
        """
        self.order_total = self.lineorders.aggregate(Sum('lineorder_total'))['lineorder_total__sum']
        if self.order_total < settings.FREE_DELIVERY:
            self.delivery_cost = self.order_total * settings.DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.shop_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self.get_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class ProductLineOrder(models.Model):
    order = models.ForeignKey(ProductOrder, null=False, blank=False, on_delete=models.CASCADE, related_name='lineorders')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
    product_quantity = models.IntegerField(null=False, blank=False, default=0)
    lineorder_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the product line order total
        and update the order total.
        """
        self.lineorder_total = self.product.price * self.product_quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

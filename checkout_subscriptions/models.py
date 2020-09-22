import uuid

from django.db import models
from django.db.models import Sum

from autoslug import AutoSlugField

from subscriptions.models import Plan
from user_profile.models import UserProfile


class SubscriptionOrder(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    plan_name = AutoSlugField(populate_from='plan_duration')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='subscription_order')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def get_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

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

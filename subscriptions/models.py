from django.db import models


class Plan(models.Model):

    class Meta:
        verbose_name_plural = 'Plan'

    plan_duration = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.plan_duration

class StripePayment(models.Model):

    class Meta:
        verbose_name_plural = 'Plan Payment'

    paymentId = models.CharField(max_length=150)
    amount = models.CharField(max_length=150)
    paid = models.BooleanField()

    def __str__(self):
        return self.paymentId
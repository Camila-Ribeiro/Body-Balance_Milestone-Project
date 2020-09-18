from django.db import models


class Nutrition(models.Model):

    class Meta:
        verbose_name_plural = 'Nutrition'

    week = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    day = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    description = models.TextField(max_length=1000)
    breakfast = models.TextField(max_length=1000)
    am_snack = models.TextField(max_length=1000)
    lunch = models.TextField(max_length=1000)
    pm_snack = models.TextField(max_length=1000)
    dinner = models.TextField(max_length=1000)
    daily_total_cal = models.DecimalField(max_digits=4, decimal_places=3)
    protein = models.CharField(max_length=100)
    carbohydrates = models.CharField(max_length=100)
    fiber = models.CharField(max_length=100)
    fat = models.CharField(max_length=100)
    sodium = models.DecimalField(max_digits=4, decimal_places=3)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)

from django.contrib import admin
from .models import Nutrition

# Register your models here.


class Nutrition_Plan_Admin(admin.ModelAdmin):
    list_display = (
        'week',
        'day',
        'image_file',
    )

admin.site.register(Nutrition, Nutrition_Plan_Admin)

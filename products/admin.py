from django.contrib import admin
from .models import Product, Category

# Register your models here.


class Product_Admin(admin.ModelAdmin):
    list_display = (
        'sku',
        'product_name',
        'category',
        'price',
        'rating',
        'image_file',
    )

    ordering = ('sku',)


class Category_Admin(admin.ModelAdmin):
    list_display = (
        'category_friendly_name',
        'category_name',
    )


admin.site.register(Product, Product_Admin)
admin.site.register(Category, Category_Admin)

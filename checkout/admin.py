from django.contrib import admin
from .models import ProductOrder, ProductLineOrder

# Register your models here.


class ProductOrderAdminInline(admin.TabularInline):
    model = ProductLineOrder
    readonly_fields = ('lineorder_total',)


class ProductOrderAdmin(admin.ModelAdmin):
    inlines = (ProductOrderAdminInline,)

    readonly_fields = ('order_number', 'purchase_date',
                       'delivery_cost', 'order_total',
                       'shop_total', 'original_shop_bag',
                       'stripe_pid',)

    fields = ('order_number', 'purchase_date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'shop_total', 'original_shop_bag',
              'stripe_pid',)

    list_display = ('order_number', 'purchase_date', 'full_name',
                    'order_total', 'delivery_cost',
                    'shop_total',)

    ordering = ('-purchase_date',)

admin.site.register(ProductOrder, ProductOrderAdmin)
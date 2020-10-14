from django.contrib import admin
from .models import ProductOrder, ProductLineOrder


class ProductOrderAdminInline(admin.TabularInline):
    model = ProductLineOrder
    readonly_fields = ('lineorder_total',)


class ProductOrderAdmin(admin.ModelAdmin):
    inlines = (ProductOrderAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'shop_total', 'original_shop_bag',
                       'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'shop_total', 'original_shop_bag',
              'stripe_pid',)
            
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'shop_total',)

    ordering = ('-date',)


# class SubscriptionOrderAdmin(admin.ModelAdmin):

#     readonly_fields = ('order_number', 'date', 'stripe_pid',)

#     fields = ('order_number', 'date', 'user_profile',
#               'full_name', 'email', 'stripe_pid',)

#     list_display = ('order_number', 'date', 'full_name',)

#     ordering = ('-date',)


admin.site.register(ProductOrder, ProductOrderAdmin)
# admin.site.register(SubscriptionOrder, SubscriptionOrderAdmin)
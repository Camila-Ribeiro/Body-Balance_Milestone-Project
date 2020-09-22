from django.contrib import admin

from .models import SubscriptionOrder

class SubscriptionOrderAdmin(admin.ModelAdmin):

    readonly_fields = ('date', 'order_number', 
                       'plan_name', 'price',
                       'stripe_pid',)

    fields = ('date', 'order_number', 'plan_name', 'user_profile',
              'full_name', 'email', 'price', 'stripe_pid',)
            

    list_display = ('date', 'order_number', 'plan_name',
                    'price',)

    ordering = ('-date',)

admin.site.register(SubscriptionOrder, SubscriptionOrderAdmin)
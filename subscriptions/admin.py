from django.contrib import admin
from .models import Plan, StripePayment


class Subscription_Admin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    list_display = (
        'plan_duration',
    )


class Stripe_Admin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    list_display = (
        'paid',
    )

admin.site.register(Plan, Subscription_Admin)
admin.site.register(StripePayment, Stripe_Admin)

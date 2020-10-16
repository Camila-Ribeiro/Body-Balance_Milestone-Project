from django.contrib import admin
from .models import Plan


class Subscription_Admin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    list_display = (
        'plan_duration',
    )

admin.site.register(Plan, Subscription_Admin)

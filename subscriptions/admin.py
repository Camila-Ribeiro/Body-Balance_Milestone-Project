from django.contrib import admin
from .models import Plan


class Subscription_Admin(admin.ModelAdmin):
    readonly_fields = ('plan_name',)

    list_display = (
        'plan_duration',
        'plan_name',
    )

admin.site.register(Plan, Subscription_Admin)
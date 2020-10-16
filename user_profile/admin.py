from django.contrib import admin
from .models import UserProfile


class HasPlanAdmin(admin.ModelAdmin):
    readonly_fields = (
        'has_plan',)

    readonly_fields = (
        'has_plan',) 

    list_display = (
        'has_plan',
    )


admin.site.register(UserProfile, HasPlanAdmin)

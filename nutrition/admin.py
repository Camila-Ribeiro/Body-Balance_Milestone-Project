from django.contrib import admin
from .models import Nutrition

class Nutrition_Plan_Admin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    list_display = (
        'plan_name',
        'week',
        'day',
    )
    ordering = ('-week', '-day',)

admin.site.register(Nutrition, Nutrition_Plan_Admin)

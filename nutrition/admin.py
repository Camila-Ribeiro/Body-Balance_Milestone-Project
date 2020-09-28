from django.contrib import admin
from .models import Nutrition


class Nutrition_Plan_Admin(admin.ModelAdmin):
    list_display = (
        'plan_name',
        'week',
        'day',
        # 'image_file',
    )
    
    ordering = ('-week', '-day',)


admin.site.register(Nutrition, Nutrition_Plan_Admin)

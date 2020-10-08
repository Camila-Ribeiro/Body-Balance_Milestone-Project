from django.contrib import admin
from .models import Nutrition

class Nutrition_Plan_Admin(admin.ModelAdmin):

    def has_add_permission(self, request):
    #     nutrition_obj = Nutrition.objects.get('day')
    #     if 'day' > 7:
            return False

    list_display = (
        'plan_name',
        'week',
        'day',
        # 'image_file',
    )
    
    ordering = ('-week', '-day',)


admin.site.register(Nutrition, Nutrition_Plan_Admin)

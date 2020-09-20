from django.contrib import admin
from .models import Workouts

# Register your models here.


class Workouts_Admin(admin.ModelAdmin):
    list_display = (
        'current_week',
        'main_goal',
        'author_name',
    )

admin.site.register(Workouts, Workouts_Admin)
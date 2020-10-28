from django.contrib import admin
from .models import UserProfile


class UserProfile_Admin(admin.ModelAdmin):

    list_display = (
        'user', 'has_plan',
    )


admin.site.register(UserProfile, UserProfile_Admin)

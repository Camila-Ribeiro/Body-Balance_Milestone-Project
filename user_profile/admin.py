from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin


class UserProfile_Admin(admin.ModelAdmin):

    list_display = (
        'user', 'has_plan',
    )

admin.site.register(UserProfile, UserProfile_Admin)
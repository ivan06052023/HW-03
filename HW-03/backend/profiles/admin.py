from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Профиль пользователя"""
    list_display = ("user", "first_name", "last_name", "email_two", "phone")
    list_filter = ("user", "first_name", "last_name", "email_two", "phone")


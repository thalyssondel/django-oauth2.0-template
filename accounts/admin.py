from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("is_banned",)

    fieldsets = UserAdmin.fieldsets + (("Punishment Control", {"fields": ("is_banned",)}),)


admin.site.register(CustomUser, CustomUserAdmin)

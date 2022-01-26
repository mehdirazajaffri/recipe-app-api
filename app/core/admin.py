from django.contrib import admin
from core import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'fav_month']
    fieldsets = ((None, {'fields': ('email', 'password')}),
                 (_('Personal Info'), {'fields': ('name',)}),
                 (_('Permissions'), {
                  'fields': ('is_active', 'is_staff', 'is_superuser')}),
                 (_('Important dates'), {'fields': ('last_login',)}),
                 (_('Favorite Months'), {'fields': ('fav_month',)}),
                 )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ('email', 'password1', 'password2', 'name', 'username', 'fav_month')
        }),
    )
    search_fields = ["email", "name"]


admin.site.register(models.User, UserAdmin)
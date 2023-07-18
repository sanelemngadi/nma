from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import NMAUserChangeForm, NMAUserCreationForm
from users.models import NMAUser

# Register your models here.

class NMAUserAdmin(UserAdmin):
    add_form = NMAUserCreationForm
    form = NMAUserChangeForm
    model = NMAUser

    list_display = ("username", "email", "is_staff", "is_active",
        "is_superuser", "last_login")

    list_filter = ("is_staff", "is_active", "is_superuser")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("permissions", {"fields": ("is_staff", "is_active", "is_superuser",
        "groups", "user_permissions")}),
        ("Dates", {"fields": ("last_login", "date_joined")})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(NMAUser, NMAUserAdmin)

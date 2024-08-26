from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from sleep.models import Sleep

from .models import CustomUser, Profile


class SleepInLine(admin.TabularInline):
    model = Sleep
    extra = 0
    readonly_fields = ["slept_at", "sleep_length"]
    ordering = ["-slept_at"]


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    inlines = [SleepInLine]
    list_display = ("id", "user_full_name", "age", "gender", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    def user_full_name(self, obj: Profile) -> str:
        return f"{obj.user.first_name.title()} {obj.user.last_name.title()}"


class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)

from django.contrib import admin

from sleep.models import Sleep

from .models import Profile


class SleepInLine(admin.TabularInline):
    model = Sleep
    extra = 0
    readonly_fields = ["slept_at", "sleep_length"]
    ordering = ["-slept_at"]


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    inlines = [SleepInLine]
    list_display = ("id", "user_full_name", "age", "gender", "created_at", "updated_at")
    readonly_fields = ('created_at', 'updated_at')

    def user_full_name(self, obj: Profile) -> str:
        return f"{obj.user.first_name.title()} {obj.user.last_name.title()}"


admin.site.register(Profile, ProfileAdmin)

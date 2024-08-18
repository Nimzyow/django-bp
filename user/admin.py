from django.contrib import admin

from .models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user_full_name", "age", "gender", "created_at", "updated_at")
    readonly_fields = ('created_at', 'updated_at')

    def user_full_name(self, obj: Profile) -> str:
        return f"{obj.user.first_name.title()} {obj.user.last_name.title()}"

from django.contrib import admin

from .models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "age", "gender", "created_at", "updated_at")
    readonly_fields = ('created_at', 'updated_at')

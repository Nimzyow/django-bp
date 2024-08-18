from django.contrib import admin

from .models import Sleep


# Register your models here.
@admin.register(Sleep)
class SleepAdmin(admin.ModelAdmin):
    list_display = ("id", "profile", "slept_at", "sleep_length")
    readonly_fields = ("created_at", "updated_at")

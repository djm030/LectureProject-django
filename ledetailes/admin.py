from django.contrib import admin
from .models import LeDetail


@admin.register(LeDetail)
class LeDetailAdmin(admin.ModelAdmin):
    list_display = (
        "lecture",
        "video",
    )

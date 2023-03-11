from django.contrib import admin
from .models import LeDetaile


@admin.register(LeDetaile)
class LeDetaileAdmin(admin.ModelAdmin):
    list_display = (
        "lecture",
        "video",
    )

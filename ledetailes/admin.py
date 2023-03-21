from django.contrib import admin
from .models import LeDetaile


@admin.register(LeDetaile)
class LeDetailAdmin(admin.ModelAdmin):
    list_display = ("lecture",)

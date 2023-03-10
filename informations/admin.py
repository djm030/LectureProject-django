from django.contrib import admin
from .models import Information
Information
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    pass
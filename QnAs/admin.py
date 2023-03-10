from django.contrib import admin
from .models import QnA


@admin.register(QnA)
class QnAadmin(admin.ModelAdmin):
    pass

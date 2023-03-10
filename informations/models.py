from django.db import models
from common.models import CommonModel


class Information(models.Model):
    sDate = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(max_length=150)
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="information",
    )

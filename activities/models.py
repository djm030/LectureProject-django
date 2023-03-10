from django.db import models
from common.models import CommonModel


class Activite(models.Model):
    loginDate = models.DateTimeField(auto_now=True)
    lectureDate = models.DateTimeField(auto_now=True)
    paymentDate = models.DateTimeField(auto_now=True)
    isWithdrawn = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    Withdrawn_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="activite",
    )
    information = models.OneToOneField(
        "informations.Information",
        on_delete=models.CASCADE,
        related_name="activities",
    )

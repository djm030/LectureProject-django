from django.db import models
from users.models import Activite


class Information(Activite):
    sDate = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(max_length=150, blank=True, null=True)
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="information",
    )

from django.db import models
from common.models import CommonModel


class LeDetaile(CommonModel):
    lecture = models.OneToOneField(
        "lectures.lecture",
        on_delete=models.CASCADE,
        related_name="ledetailes",
    )
    like = models.BooleanField(default=False)

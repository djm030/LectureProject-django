from django.db import models
from common.models import CommonModel


class numCart(CommonModel):
    lecture = models.ForeignKey(
        "lectures.Lecture",
        related_name="cart",
        null=True,
    )

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="cart",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "Cart"

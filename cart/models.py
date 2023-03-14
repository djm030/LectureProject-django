from django.db import models
from common.models import CommonModel


class Cart(CommonModel):
    lecture = models.ManyToManyField(
        "lectures.Lecture",
        related_name="cart",
        blank=True,
        null=True,
    )
    rating = models.CharField(
        max_length=10,
        blank=True,
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

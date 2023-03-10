from django.db import models
from common.models import CommonModel


class Cart(CommonModel):
    lecture = models.ForeignKey(
        "lectures.Lecture",
        on_delete=models.CASCADE,
    )
    rating = models.CharField(max_length=10)

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="cart",
    )

    class Meta:
        verbose_name_plural = "Cart"
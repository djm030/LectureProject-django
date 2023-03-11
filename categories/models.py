from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    classification = models.CharField(
        max_length=100,
    )
    name = models.CharField(
        max_length=100,
    )
    order = models.CharField(
        max_length=100,
    )

    class Meta:
        verbose_name_plural = "Categories"

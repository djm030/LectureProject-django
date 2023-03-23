from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=400)
    email = models.EmailField(max_length=200)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "accounts"

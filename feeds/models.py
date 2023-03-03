from django.db import models

class Feed(models.Model):
    name = models.CharField(max_length=150)
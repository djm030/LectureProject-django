from django.db import models
from common.models import CommonModel


# Create your models here.
class Lecture(CommonModel):
    class Difficulty(models.IntegerChoices):
        pass

    lectureTitle = models.CharField(max_length=100)
    lectureDifficulty = models.CharField(max_length=100)
    lectureDescription = models.TextField(max_length=1000)
    lectureDifficulty = models.CharField(max_length=100)
    targetAudience = models.CharField(max_length=100)
    lectureFee = models.PositiveIntegerField(blank=True, null=True,)
    thumbnail = models.URLField(blank=True, null=True,)
    lecturePeriod = models.DateField(blank=True, null=True,)
    isOpened = models.BooleanField(default=True)
    likes = models.BooleanField(default=True)
    lectureDuration = models.PositiveIntegerField(blank=True, null=True,)
    lectureTotal = models.CharField(max_length=100, blank=True, null=True,)

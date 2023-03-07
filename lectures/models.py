from django.db import models
from common.models import CommonModel


# Create your models here.
class Lecture(CommonModel):
    class Difficulty(models.IntegerChoices):
        pass

    LectureTitle = models.CharField(max_length=100)
    LectureDifficulty = models.CharField(max_length=100)
    LectureDescription = models.TextField(max_length=1000)

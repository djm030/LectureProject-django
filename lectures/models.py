from django.db import models
from common.models import CommonModel

# 회원번호
# 강의번호
# 강의제목
# 강의설명
# 강의난이도
# 강의대상자
# 수강료
# 썸네일
# 수강기간
# 개설여부
# 강의시간
# 좋아요
# 총강의갯수


# Create your models here.
class Lecture(CommonModel):
    class Difficulty(models.TextChoices):
        EASY = (
            "easy",
            "Easy",
        )
        MIDDLE = (
            "middle",
            "Middle",
        )
        HARD = (
            "hard",
            "Hard",
        )

    LectureId = models.AutoField(primary_key=True)

    lectureTitle = models.CharField(max_length=100)
    lectureDifficulty = models.CharField(max_length=100)
    lectureDescription = models.TextField(max_length=1000)
    lectureDifficulty = models.CharField(max_length=100)
    targetAudience = models.CharField(max_length=100)
    lectureFee = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    thumbnail = models.URLField(
        blank=True,
        null=True,
    )
    lecturePeriod = models.DateField(
        blank=True,
        null=True,
    )
    isOpened = models.BooleanField(default=True)
    likes = models.PositiveIntegerField(null=True, blank=True)
    lectureDuration = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    lectureTotal = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    instructor = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="lectures",
    )

    categories = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="ledetailes",
    )
    grade = models.PositiveIntegerField()

    def __str__(self):
        return self.lectureTitle


class calculatedLecture(CommonModel):
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name="lecture",
    )

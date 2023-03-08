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
    lectureDifficulty = models.CharField(
        max_length=20,
        choices=Difficulty.choices,
    )
    lectureDescription = models.TextField(max_length=1000)
    targetAudience = models.CharField(max_length=30)
    lectureFee = models.PositiveIntegerField()
    thumbnail = models.URLField()
    lecturePeriod = models.DurationField()
    isOpened = models.BooleanField(default=True)
    # 강의기간
    lectureDuration = models.PositiveIntegerField(default=0)
    # 강의 총 갯수
    lectureTotal = models.PositiveIntegerField(default=0)
    # 좋아요 갯수
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.lectureTitle


class calculatedLecture(CommonModel):
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name="lecture_details",
    )

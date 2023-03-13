from django.db import models
from common.models import CommonModel
from lectures.models import Lecture
from users.models import User

# Create your models here.
"""
작성자 (Author)
강의명 (Course)
교수명 (Professor)
평점 (Rating)
내용 (Content)

"""


class Review(CommonModel):
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    title = models.CharField(
        max_length=30,
    )
    rating = models.PositiveSmallIntegerField()
    content = models.TextField()

    def __str__(self):
        return self.title

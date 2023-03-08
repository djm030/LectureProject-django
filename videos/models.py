from django.db import models
from common.models import CommonModel


class Video(CommonModel):

    title = models.CharField(max_length=100)
    lecture = models.ForeignKey(
        "lectures.Lecture",
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    videoFile = models.URLField()
    videoLength = models.IntegerField(default=0)

    def __str__(self):
        return self.title

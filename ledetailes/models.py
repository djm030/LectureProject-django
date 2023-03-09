from django.db import models
from common.models import CommonModel


class LeDetaile(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    lecture = models.ForeignKey("lectures.Lecture", on_delete=models.CASCADE)
    video = models.ForeignKey("videos.Video", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

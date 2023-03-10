from django.db import models
from common.models import CommonModel


class LeDetaile(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    lecture = models.OneToOneField("lectures.lecture", on_delete=models.CASCADE)
    video = models.OneToOneField("videos.Video", on_delete=models.CASCADE, related_name="video")

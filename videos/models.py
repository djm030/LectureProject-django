from django.db import models
from common.models import CommonModel


class Video(CommonModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to="videos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models
from common.models import CommonModel
from users.models import User

# Create your models here.

"""
  제목
  내용
  작성자
  좋아요
"""


class QnA(CommonModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="qnas")
    like_users = models.ManyToManyField(User, blank=True, related_name="like_qnas")

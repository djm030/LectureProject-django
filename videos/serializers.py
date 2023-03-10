from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Video


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

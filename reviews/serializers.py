from rest_framework import serializers
from .models import Review, Reply
from users.serializers import OneUserSerializer


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    reply = ReplySerializer(many=True)

    class Meta:
        model = Review
        fields = (
            "user",
            "lecture",
            "title",
            "rating",
            "content",
            "reply",
        )

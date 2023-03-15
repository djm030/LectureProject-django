from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import OneUserSerializer


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

from rest_framework import serializers
from .models import LeDetail


class LedetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeDetail
        fields = "__all__"

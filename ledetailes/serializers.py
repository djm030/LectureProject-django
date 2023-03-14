from rest_framework import serializers
from .models import LeDetaile


class LedetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeDetaile
        fields = "__all__"

from rest_framework import serializers

from user.models import Profile

from .models import Sleep


class SleepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sleep
        fields = ["slept_at", "sleep_length"]

from datetime import datetime, time
from typing import TypedDict

from django.utils.timezone import make_aware, now
from rest_framework import serializers

from user.models import Profile

from .models import Sleep


class SleepData(TypedDict):
    slept_at: str
    sleep_length: float


class SleepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sleep
        fields = ["slept_at", "sleep_length"]

    def validate_slept_at(self, value):
        today_start = make_aware(datetime.combine(now().date(), time.min))
        if value >= today_start:
            raise serializers.ValidationError("The 'slept_at' date must be before today at 00:00:00")
        return value

    def create(self, validated_data: SleepData) -> Sleep:
        profile_instance = validated_data["profile"]
        slept_at = validated_data["slept_at"]

        sleep_instance = Sleep.objects.filter(profile=profile_instance, slept_at=slept_at).first()

        if sleep_instance:
            sleep_instance.sleep_length = validated_data["sleep_length"]
            sleep_instance.save()
            return sleep_instance
        else:
            return Sleep.objects.create(**validated_data)

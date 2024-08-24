from rest_framework import serializers

from user.models import Profile

from .models import Sleep


class SleepSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())

    class Meta:
        model = Sleep
        fields = ["slept_at", "sleep_length"]

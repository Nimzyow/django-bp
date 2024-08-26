from typing import TypedDict

from rest_framework import serializers

from sleep.models import Sleep

from .models import CustomUser, Profile


class ProfileData(TypedDict):
    age: int
    gender: str


class UserCreationData(TypedDict):
    first_name: str
    last_name: str
    email: str
    password: str
    profile: ProfileData


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["age", "gender"]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    sleep_entries = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "profile",
            "sleep_entries",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: UserCreationData) -> CustomUser:

        profile_data: ProfileData = validated_data.pop("profile")
        password: str = validated_data.pop("password")

        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        Profile.objects.create(user=user, **profile_data)
        return user

    def get_sleep_entries(self, obj: CustomUser) -> int:
        return Sleep.objects.filter(profile=obj.profile).count()

from typing import TypedDict

from rest_framework import serializers

from .models import Profile, User


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
        fields = ['age', 'gender']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "profile"]

    def create(self, validated_data: UserCreationData) -> User:
        profile_data: ProfileData = validated_data.pop("profile")
        password: str = validated_data.pop("password")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        Profile.objects.create(user=user, **profile_data)
        return user

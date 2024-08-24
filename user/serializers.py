from rest_framework import serializers

from .models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['age', 'gender']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        password = validated_data.pop("password")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        Profile.objects.create(user=user, **profile_data)
        return user

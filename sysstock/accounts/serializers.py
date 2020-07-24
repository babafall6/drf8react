from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile

# Profile Serialization
class ProfilSerialization(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ("id", "username", "email", "profile")


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfilSerialization()

    class Meta:
        model = User
        fields = ("id", "username", "password", "profile")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        user = User.objects.create_user(
            validated_data["username"], validated_data["password"]
        )
        Profile.objects.create(user=user, **profile_data)
        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

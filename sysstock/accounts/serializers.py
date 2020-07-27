from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile
import re


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ("id", "username", "email", "profile")


# ProfileSerializer
class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Profile
        fields = ["id", "privilege", "user"]
        read_only_fields = ("user",)


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "password", "profile"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        user = User.objects.create_user(**validated_data)

        Profile.objects.create(user=user, **profile_data)

        return user

    def validate_username(self, value):
        """
            Verifier que le username a un format 
            numero telephone de 9 chiffres
            du senegal
        """
        pattern = re.compile(r"\b7(0|6|7|8)\d{7}\b")
        if not pattern.match(value):
            raise serializers.ValidationError(
                "La valeur doit etre un numero telephone Senegal."
            )
        return value


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

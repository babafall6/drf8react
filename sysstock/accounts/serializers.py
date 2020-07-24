from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import MyUser
import re


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ("id", "username", "full_name")


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ("id", "username", "email", "full_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_username(self, value):
        """
            Verifier que le username a un format 
            numero telephone de 9 chiffres
            du senegal
        """
        pattern = re.compile(r"\b7(0|6|7|8)\d{7}\b")
        if not pattern.match(value):
            raise serializers.ValidationError("It must be a valide phone number.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["full_name"],
            validated_data["password"],
        )
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

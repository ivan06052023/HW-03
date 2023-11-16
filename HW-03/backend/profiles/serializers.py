
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSer(serializers.ModelSerializer):
    """сериализация пользователя"""
    class Meta:
        model = User
        fields = ("username", "email")


class ProfileDetailSer(serializers.ModelSerializer):
    """Профиль пользователя"""
    user = UserSer()

    class Meta:
        model = Profile
        fields = (
            "user",
            "avatar",
            "email_two",
            "phone",
            "first_name",
            "last_name",
            "middle_name",
        )

class ProfileUpdateSer(serializers.ModelSerializer):
    """Редактирование профиля пользователя"""

    class Meta:
        model = Profile
        fields = (
            "avatar",
            "email_two",
            "phone",
            "first_name",
            "last_name",
            "middle_name",
        )

class AvatarUpdateSer(serializers.ModelSerializer):
    """Редактирование аватар пользователя"""
    class Meta:
        model = Profile
        fields = ("avatar",)
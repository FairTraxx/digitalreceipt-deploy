from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User


class UserCreateSerializers(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email', 'phone', 'password')
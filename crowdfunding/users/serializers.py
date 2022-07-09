from unittest.util import _MAX_LENGTH
from django.http import Http404, HttpResponseBadRequest
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=True)
    password = serializers.CharField(max_length=50)

    def create(self, validated_data):
        try:
            validated_data['password'] = make_password(validated_data['password'])
            return CustomUser.objects.create(**validated_data)
        except KeyError:
            raise HttpResponseBadRequest


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if "password" in validated_data.keys():
            instance.password = make_password(validated_data.get('password'))
        instance.save()
        return instance

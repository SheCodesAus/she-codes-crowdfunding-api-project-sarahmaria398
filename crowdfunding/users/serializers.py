from unittest.util import _MAX_LENGTH
from wsgiref import validate
from django.http import Http404, HttpResponseBadRequest
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=True)
    password = serializers.CharField(max_length=200)
    image = serializers.URLField(max_length=300, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
    bio = serializers.CharField(default="Write bio here.")

    def create(self, validated_data):
        try:
            validated_data['password'] = make_password(validated_data['password'])
            return CustomUser.objects.create(**validated_data)
        except KeyError:
            raise HttpResponseBadRequest


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.image = validated_data.get('image', instance.image)
        instance.bio = validated_data.get('bio', instance.bio)
        if "password" in validated_data.keys():
            instance.password = make_password(validated_data.get('password'))
        instance.save()
        return instance

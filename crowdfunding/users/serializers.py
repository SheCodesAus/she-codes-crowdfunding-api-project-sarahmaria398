from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get(validated_data['username'])
        instance.email = validated_data.get(validated_data['email'])
        return instance

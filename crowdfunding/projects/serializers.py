from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Project

class ProjectSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.TimeField()
    image = serializers.URLField()
    date_created = serializers.DateTimeField()
    owner = serializers.CharField(max_length=200)


    def create(self,validated_data):
        return Project.objects.create(**validated_data)


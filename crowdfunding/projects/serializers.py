from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Project, Pledge



class PledgeSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.TimeField()
    comment = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()
    supporter = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.TimeField()
    image = serializers.URLField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    
    def create(self,validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializers):
    pledges = PledgeSerializers(many=True, read_only=True)
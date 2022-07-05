from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Project, Pledge



class PledgeSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.TimeField()
    comment = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()
    supporter = serializers.ReadOnlyField(source='supporter.id')

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


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


class PledgeDetailSerializer(PledgeSerializers):
    pledges = PledgeSerializers(many=True, read_only=True)


    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment',instance.comment)
        
        instance.project = validated_data.get('project', instance.project)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.save()
        return instance
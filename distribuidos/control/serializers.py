from rest_framework import serializers
from .models import Faculty,Person,Section,School,Enrollment
from django.utils.timezone import now


class FacultySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20, required=False)
    description = serializers.CharField(max_length=30, required=False)
    status = serializers.CharField(default='enabled', max_length=50, required=False)
    created_date = serializers.DateTimeField(default=now, required=False)
    deleted_date = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Faculty` instance, given the validated data.
        """
        return Faculty.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Faculty` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dni = serializers.CharField(max_length=20, required=False)
    firt_name = serializers.CharField(max_length=20, required=False)
    last_name = serializers.CharField(max_length=20, required=False)
    status = serializers.CharField(default='enabled', max_length=50, required=False)
    created_date = serializers.DateTimeField(default=now, required=False)
    deleted_date = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Person` instance, given the validated data.
        """
        return Person.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Person` instance, given the validated data.
        """
        instance.dni = validated_data.get('dni', instance.dni)
        instance.firt_name = validated_data.get('firt_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

class SchoolSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50, required=False)
    description = serializers.CharField(max_length=50, required=False)
    status = serializers.CharField(default='enabled', max_length=50, required=False)
    created_date = serializers.DateTimeField(default=now, required=False)
    deleted_date = serializers.DateTimeField(required=False)
    fk_facultad_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `School` instance, given the validated data.
        """
        return School.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `School` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.fk_facultad = validated_data.get('fk_facultad', instance.fk_facultad)
        instance.save()
        return instance

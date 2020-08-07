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



















"""class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['id',
                  'status',
                  'created_date',
                  'deleted_date',
                  'dni',
                  'firt_name',
                  'last_name']

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['id',
                  'status',
                  'created_date',
                  'deleted_date',
                  'name',
                  'description',
                  'facultad_id']

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ['id',
                  'status',
                  'created_date',
                  'deleted_date',
                  'name',
                  'description',
                  'uc',
                  'semester',
                  'tipo',
                  'ht',
                  'hp',
                  'hl',
                  'school_id']

class EnrollmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id',
                  'status',
                  'created_date',
                  'deleted_date',
                  'type']
"""
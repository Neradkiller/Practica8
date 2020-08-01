from rest_framework import serializers
from .models import Faculty,Person,Section,School

class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id',
                  'status',
                  'fecha_creacion',
                  'fecha_eliminacion',
                  'name',
                  'description']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['id',
                  'status',
                  'fecha_creacion',
                  'fecha_eliminacion',
                  'dni',
                  'firt_name',
                  'last_name']

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['id',
                  'status',
                  'fecha_creacion',
                  'fecha_eliminacion',
                  'name',
                  'description',
                  'facultad_id']

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ['id',
                  'status',
                  'fecha_creacion',
                  'fecha_eliminacion',
                  'name',
                  'description',
                  'uc',
                  'semester',
                  'tipo',
                  'ht',
                  'hp',
                  'hl',
                  'school_id']
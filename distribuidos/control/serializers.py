from rest_framework import serializers
from .models import Faculty,Person,Section,School,Enrollment
from django.utils.timezone import now


class FacultySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20, required=False)
    description = serializers.CharField(max_length=50, required=False)
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
        instance.firt_name = validated_data.get('firt_name', instance.firt_name)
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
        instance.fk_facultad_id = validated_data.get('fk_facultad_id', instance.fk_facultad_id)
        instance.save()
        return instance

class SectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50, required=False)
    description = serializers.CharField(max_length=70, required=False)
    status = serializers.CharField(default='enabled', max_length=50, required=False)
    created_date = serializers.DateTimeField(default=now, required=False)
    deleted_date = serializers.DateTimeField(required=False)
    uc = serializers.IntegerField(required=False)
    semester = serializers.IntegerField(required=False)
    tipo = serializers.CharField(default = 'mandatory',max_length=9, required=False)
    ht = serializers.DecimalField(required=False,max_digits=4, decimal_places = 2)
    hp = serializers.DecimalField(required=False,max_digits=4, decimal_places = 2)
    hl = serializers.DecimalField(required=False,max_digits=4, decimal_places = 2)
    fk_school_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Section` instance, given the validated data.
        """
        return Section.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Section` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.uc = validated_data.get('uc', instance.uc)
        instance.semester = validated_data.get('semester', instance.semester)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.ht = validated_data.get('ht', instance.ht)
        instance.hp = validated_data.get('hp', instance.hp)
        instance.hl = validated_data.get('hl', instance.hl)
        instance.save()
        return instance

class EnrollmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    fk_person_id = serializers.IntegerField(required=False)
    fk_section_id = serializers.IntegerField(required=False)
    tipo = serializers.CharField(max_length=8, required=False)
    status = serializers.CharField(default='enabled', max_length=10, required=False)
    created_date = serializers.DateTimeField(default=now, required=False)
    deleted_date = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Enrollment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fk_person_id = validated_data.get('fk_person_id', instance.fk_person_id)
        instance.fk_section_id = validated_data.get('fk_section_id', instance.fk_section_id)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.save()
        return instance

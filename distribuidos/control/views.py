from django.shortcuts import render
from rest_framework import viewsets
from .models import Faculty,Person,Section,School
from .serializers import FacultySerializer,PersonSerializer,SchoolSerializer,SectionSerializer
# Create your views here.

class FacultyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Facultys to be viewed or edited.
    """
    queryset = Faculty.objects.all().order_by('id')
    serializer_class = FacultySerializer

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Persons to be viewed or edited.
    """
    queryset = Person.objects.all().order_by('id')
    serializer_class = PersonSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Schhol to be viewed or edited.
    """
    queryset = School.objects.all().order_by('id')
    serializer_class = SchoolSerializer

class SectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Section to be viewed or edited.
    """
    queryset = Section.objects.all().order_by('id')
    serializer_class = SectionSerializer
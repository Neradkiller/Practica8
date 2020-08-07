from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.timezone import now

from .models import Faculty
from .serializers import FacultySerializer

# Create your views here.

@api_view(['GET', 'POST'])
def faculty_list(request):

    if request.method == 'GET':
        facultys = Faculty.objects.filter(status='enabled')
        serializer = FacultySerializer(facultys, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def faculty_detail(request, pk):

    try:
        faculty = Faculty.objects.get(id=pk, status='enabled')
    except Faculty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FacultySerializer(faculty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        faculty.status = 'disabled'
        faculty.deleted_date = now()
        faculty.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

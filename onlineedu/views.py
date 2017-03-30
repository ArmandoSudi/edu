from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers

from onlineedu.models import University, Department ,Course
from onlineedu.models import CourseMaterial, VideoURL ,Book
from onlineedu.serializers import UniversitySerializer, DepartmentSerializer
from onlineedu.serializers import CourseSerializer, CourseMaterialSerializer
from onlineedu.serializers import BookSerializer, VideoURLSerializer

class UniversityList(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseMaterialList(generics.ListCreateAPIView):
    queryset = CourseMaterial.objects.all()
    serializer_class = CourseMaterialSerializer

class VideoURLList(generics.ListCreateAPIView):
    queryset = VideoURL.objects.all()
    serializer_class = BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

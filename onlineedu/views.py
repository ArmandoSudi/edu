from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers

from onlineedu.models import University, Department, Course, Student, Book
from onlineedu.serializers import UniversitySerializer, DepartmentSerializer
from onlineedu.serializers import CourseSerializer, StudentSerializer
from onlineedu.serializers import BookSerializer

class UniversityList(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

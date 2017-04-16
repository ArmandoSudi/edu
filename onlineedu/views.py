from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers

from onlineedu.models import University, Department ,Course
from onlineedu.models import CourseMaterial, VideoURL ,Book
from onlineedu.serializers import UniversitySerializer, DepartmentSerializer
from onlineedu.serializers import CourseSerializer, CourseMaterialSerializer
from onlineedu.serializers import BookSerializer, VideoURLSerializer

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

def index(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    template = loader.get_template('onlineedu/index.html')
    context = {
        'university' : university,
    }
    return HttpResponse(template.render(context, request))
    
class UniversityList(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UniversityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseMaterialList(generics.ListCreateAPIView):
    queryset = CourseMaterial.objects.all()
    serializer_class = CourseMaterialSerializer

class CourseMaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseMaterial.objects.all()
    serializer_class = CourseMaterialSerializer

class VideoURLList(generics.ListCreateAPIView):
    queryset = VideoURL.objects.all()
    serializer_class = BookSerializer

class VideoURLDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoURL.objects.all()
    serializer_class = BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import serializers
from onlineedu.models import University, Department , Course
from onlineedu.models import CourseMaterial, Book, VideoURL

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class VideoURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoURL
        fields = '__all__'

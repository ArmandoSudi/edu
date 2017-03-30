from django.contrib import admin

from .models import University
from .models import Department
from .models import CourseMaterial
from .models import Course
from .models import VideoURL
from .models import Book

class UniversityAdmin(admin.ModelAdmin):
    model = University

class DepartmentAdmin(admin.ModelAdmin):
    model = Department

class CourseAdmin(admin.ModelAdmin):
    model = Course

class CourseMaterialAdmin(admin.ModelAdmin):
    model = CourseMaterial

class VideoURLAdmin(admin.ModelAdmin):
    model = VideoURL

class BookAdmin(admin.ModelAdmin):
    model = Book


admin.site.register(University, UniversityAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseMaterial, CourseMaterialAdmin)
admin.site.register(VideoURL, VideoURLAdmin)
admin.site.register(Book, BookAdmin)

from django.contrib import admin

from .models import University
from .models import Department
from .models import Course
from .models import Student
from .models import Book

class UniversityAdmin(admin.ModelAdmin):
    model = University

class DepartmentAdmin(admin.ModelAdmin):
    model = Department

class CourseAdmin(admin.ModelAdmin):
    model = Course

class StudentAdmin(admin.ModelAdmin):
    model = Student

class BookAdmin(admin.ModelAdmin):
    model = Book


admin.site.register(University, UniversityAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Book, BookAdmin)

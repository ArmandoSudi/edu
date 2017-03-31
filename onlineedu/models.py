from django.db import models

class University(models.Model):
    name = models.CharField(max_length=30)
    town = models.CharField(max_length=20, blank=True)
    logo = models.charfield(max_length=200)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    universities = models.ManyToManyField(University, related_name="departments")

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(help_text="A brief description of the course")
    departments = models.ForeignKey(Department, on_delete=models.CASCADE,
                    related_name="courses")

    def __str__(self):
        return self.name

class CourseMaterial(models.Model):
    name = models.CharField(max_length=30)
    course = models.OneToOneField(Course, related_name="course_material")
    pdf = models.CharField(max_length=20)
    word_doc = models.CharField(max_length=20)

    def __str___(self):
        return self.name

class VideoURL(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    course_material = models.ForeignKey(CourseMaterial,
        related_name="video_urls")

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    isbn = models.CharField(max_length=30)
    course_materials = models.ManyToManyField(CourseMaterial, related_name="books")

    def __str__(self):
        return self.name

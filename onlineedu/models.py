from django.db import models

class University(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    student_id = models.CharField(max_length=20)
    email = models.EmailField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name

class Book(models.Model):
    name = models.CharField(max_length=50)
    book_id = models.CharField(max_length=20)
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.name

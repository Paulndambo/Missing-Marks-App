from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# Create your models here.
TITLE_CHOICES = (
    ("Mr.", "Mr."),
    ("Dr.", "Dr."),
    ("Prof.", "Prof."),
    ("Ms.", "Ms."),
)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Binary", "Binary"),
    ("I prefer not to say", "I prefer not to say")
)

EMPLOYMENT_CHOICES = (
    ("Full-time", "Full-time"),
    ("Part-time", "Part-time"),
)

YEAR_CHOICES = (
    ("First Year", "First Year"),
    ("Second Year", "Second Year"),
    ("Third Year", "Third Year"),
    ("Fourth Year", "Fourth Year"),
    ("Fifth Year", "Fifth Year"),
)

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id_number = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=30, choices=TITLE_CHOICES)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    postal_code = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    employment_date = models.DateTimeField(default=timezone.now)
    employment_type = models.CharField(max_length=200, choices=EMPLOYMENT_CHOICES)
    education_qualifications = models.TextField()
    schools_attended = models.TextField()
    places_worked = models.TextField()

    def __str__(self):
        return self.title + " "+ self.name

    def fullname(self):
        return self.title +". "+self.name

    def get_address(self):
        return self.postal_code +" - "+ self.zip_code+" - "+self.city + ", "+self.country

    def get_absolute_url(self):
        return reverse_lazy("profile")

class Department(models.Model):
    department_name = models.CharField(max_length=500)
    school = models.CharField(max_length=500)
    offices = models.CharField(max_length=500)

    def __str__(self):
        return self.department_name
    
    def get_absolute_url(self):
        return reverse_lazy("departments")

class Programme(models.Model):
    title = models.CharField(max_length=500)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy("programmes")
    
    
class Unit(models.Model):
    unit_code = models.CharField(max_length=200, unique=True)
    unit_title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit_code

    def get_absolute_url(self):
        return reverse_lazy("units")

class AcademicYear(models.Model):
    academic_year = models.CharField(max_length=20)

    def __str__(self):
        return self.academic_year
    
    def get_absolute_url(self):
        return reverse_lazy("academic_year")
    
class Semester(models.Model):
    semester_code = models.CharField(max_length=200)
    semester_name = models.CharField(max_length=200)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)

    def __str__(self):
        return self.semester_name + " " + self.academic_year.academic_year
    
    def get_absolute_url(self):
        return reverse_lazy("semesters")


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=200, unique=True)
    full_name = models.CharField(max_length=200)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy("profile")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = ("All Students")
    

class MissingMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    year_of_study = models.CharField(max_length=200, choices=YEAR_CHOICES)

    def __str__(self):
        return self.student.full_name    
   
    def get_absolute_url(self):
        return reverse_lazy("profile")

    class Meta:
        verbose_name_plural = ("Missing Marks")
    


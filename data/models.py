from django.db import models
from django.utils import timezone
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

class Department(models.Model):
    department_name = models.CharField(max_length=500)
    school = models.CharField(max_length=500)
    offices = models.CharField(max_length=500)

    def __str__(self):
        return self.department_name

class Programme(models.Model):
    title = models.CharField(max_length=500)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Unit(models.Model):
    unit_code = models.CharField(max_length=200, unique=True)
    unit_title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit_code +" " + self.unit_title

class AcademicYear(models.Model):
    academic_year = models.CharField(max_length=20)

    def __str__(self):
        return self.academic_year
    
class Semester(models.Model):
    semester_code = models.CharField(max_length=200)
    semester_name = models.CharField(max_length=200)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)

    def __str__(self):
        return self.semester_name + " " + self.academic_year.academic_year

class MissingMark(models.Model):
    registration_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    year_of_study = models.CharField(max_length=200, choices=YEAR_CHOICES)

    def __str__(self):
        return self.name + " "+self.registration_number
    
    
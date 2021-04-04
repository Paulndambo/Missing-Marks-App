from django.contrib import admin
from . models import Lecturer, Department, AcademicYear, Programme, Unit, Semester, MissingMark, Student
# Register your models here.
admin.site.register(Lecturer)
admin.site.register(AcademicYear)
admin.site.register(Programme)
admin.site.register(Unit)
admin.site.register(Semester)
admin.site.register(Department)
admin.site.register(MissingMark)
admin.site.register(Student)

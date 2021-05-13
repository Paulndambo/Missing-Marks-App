from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView
from . models import MissingMark, Lecturer, Unit, Programme, Semester, AcademicYear, Department, Student
from . forms import MissingMarkForm, CreateStudentForm
# Create your views here.
def student_profile(request):
    student = Student.objects.get(user = request.user.id)
    student_missing_marks = MissingMark.objects.filter(student_id = student)
    context = {
        "student_missing_marks": student_missing_marks
    }
    return render(request, "profile.html", context)

class StudentCreateView(CreateView):
    form_class = CreateStudentForm
    template_name = "create_profile.html"

class MissingMarksListView(ListView):
    model = MissingMark
    fields = ('__all__')
    template_name = "missing_marks.html"

class DepartmentListView(ListView):
    model = Department
    template_name = "data/departments.html"

class DepartmentCreateView(CreateView):
    model = Department
    fields = ('__all__')
    template_name = "data/add_department.html"

class AcademicYearListView(ListView):
    model = AcademicYear
    template_name = "data/academic_years.html"

class AcademicYearCreateView(CreateView):
    model = AcademicYear
    fields = ('__all__')
    template_name = "data/add_academic_year.html"

class SemesterListView(ListView):
    model = Semester
    template_name = "data/semesters.html"

class SemesterCreateView(CreateView):
    model = Semester
    fields = ('__all__')
    template_name = "data/add_semester.html"

class ProgrammesListView(ListView):
    model = Programme
    template_name = "data/programmes.html"

class ProgrammeCreateView(CreateView):
    model  = Programme
    fields = ('__all__')
    template_name = "data/add_programme.html"

class UnitsListView(ListView):
    model = Unit
    template_name = "data/units.html"

class UnitCreateView(CreateView):
    model = Unit
    fields = ('__all__')
    template_name = "data/add_unit.html"

def home(request):
    return render(request, "index.html")

class MissingMarksCreateView(CreateView):
    form_class= MissingMarkForm
    template_name = "AddMissingMark.html"


def success_page(request):
    return render(request, "success.html")

"""
def index(request):
    return render(request, "index.html")

def create_missing_mark(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MissingMarkForm()
        else:
            missing_mark = MissingMark.objects.get(pk=id)
            form = MissingMarkForm(instance=missing_mark)
        return render(request, "AddMissingMark.html", {"form": form})
    else:
        if id == 0:
            form = MissingMarkForm(request.POST)
        else:
            missing_mark = MissingMark.objects.get(pk=id)
            form = MissingMarkForm(request.POST, instance=missing_mark)
        if form.is_valid():
            form.save()
        return redirect('/')
"""

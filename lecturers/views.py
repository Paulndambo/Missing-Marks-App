from django.shortcuts import render
from data.models import Lecturer, MissingMark
from django.views.generic import UpdateView, CreateView, ListView, DetailView
from . forms import CreateLecturerForm
# Create your views here.
def lecturer_profile(request):
    lecturer = Lecturer.objects.get(user=request.user.id)
    lecturer_missing_marks = MissingMark.objects.filter(lecturer_id = lecturer)
    context = {
        "lec_missing_marks": lecturer_missing_marks
    }
    return render(request, "lecturers/lecturer_profile.html", context)



class LecturersListView(ListView):
    model = Lecturer
    template_name ="lecturers/lecturers_list.html"

class LecturerDetailsView(DetailView):
    model = Lecturer
    template_name = "lecturers/lecturer_details.html"


class LecturerCreateView(CreateView):
    model = Lecturer
    #fields = '__all__'
    form_class = CreateLecturerForm
    template_name = "lecturers/add_lecturer.html"

class EditLecturerView(UpdateView):
    model = Lecturer
    fields = '__all__'
    template_name = "lecturers/edit_lecturer.html"

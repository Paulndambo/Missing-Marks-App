from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import MissingMark
from . forms import MissingMarkForm
# Create your views here.
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

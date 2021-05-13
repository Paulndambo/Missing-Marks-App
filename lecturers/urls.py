from django.urls import path
from . import views
from .views import LecturerCreateView, LecturersListView

urlpatterns = [
    path("", LecturersListView.as_view(), name="lecturers"),
    path("add_lecturer/", LecturerCreateView.as_view(), name="add_lecturer"),
    path("lecturer_profile/", views.lecturer_profile, name="lecturer_profile"),
]

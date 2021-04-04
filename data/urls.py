from django.urls import path
from . import views
from . views import MissingMarksCreateView, DepartmentCreateView, DepartmentListView, AcademicYearListView, AcademicYearCreateView, SemesterCreateView, SemesterListView
from . views import ProgrammesListView, StudentCreateView, MissingMarksListView, ProgrammeCreateView, UnitsListView, UnitCreateView, LecturerDetailView, LecturerCreateView, LecturersListView

urlpatterns = [
    path("", views.home, name="home"),
    path("create_missing_mark/", MissingMarksCreateView.as_view(),
         name="create_missing_mark"),
    path("success_page/", views.success_page, name="success_page"),

    path("profile/", views.user_profile, name="profile"),
    path("create_student/", StudentCreateView.as_view(), name="create_student"),

    path("lecturers/", LecturersListView.as_view(), name="lecturers"),
    path("add_lecturer/", LecturerCreateView.as_view(), name="add_lecturer"),
    path("lecturer_details/<int:pk>/", LecturerDetailView.as_view(), name="lecturer_details"),

    path("departments/", DepartmentListView.as_view(), name="departments"),
    path("add_department/", DepartmentCreateView.as_view(), name="add_department"),

    path("units/", UnitsListView.as_view(), name="units"),
    path("add_unit/", UnitsListView.as_view(), name="add_unit"),

    path("academic_years/", AcademicYearListView.as_view(), name="academic_year"),
    path("add_academic_year/", AcademicYearCreateView.as_view(), name="add_academic_year"),

    path("semesters/", SemesterListView.as_view(), name="semesters"),
    path("add_semester/", SemesterCreateView.as_view(), name="add_semester"),

    path("programmes/", ProgrammesListView.as_view(), name="programmes"),
    path("add_programme/", ProgrammeCreateView.as_view(), name="add_programme"),

    path("missing_marks/", MissingMarksListView.as_view(), name="missing_marks"),
]

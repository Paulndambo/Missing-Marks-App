from django.urls import path
from . import views

urlpatterns = [
    path("create_missing_mark/", views.create_missing_mark,
         name="create_missing_mark"),
    path("", views.index, name="index")
]

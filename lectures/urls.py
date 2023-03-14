from django.urls import path
from . import views

urlpatterns = [
    path("", views.Lectures.as_view()),
    path("<int:pk>", views.LecturesDetail.as_view()),
    path("<str:username>", views.InstructorName.as_view()),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.LectureList.as_view()),
]



from django.urls import path
from . import views

urlpatterns = [
    path("", views.InformationView.as_view()),
]

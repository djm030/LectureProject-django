from django.urls import path
from . import views

urlpatterns = [
    path("", views.LeDetailView.as_view()),
]

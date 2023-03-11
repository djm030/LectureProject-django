from django.urls import path
from . import views

urlpatterns = [
    path("", views.Activite2.as_view()),
]

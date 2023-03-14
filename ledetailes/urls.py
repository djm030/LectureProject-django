from django.urls import path
from . import views

urlpatterns = [
    path("", views.LeDetail.as_view()),
]

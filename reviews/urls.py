from django.urls import path
from . import views

urlpatterns = [
    path("<str:username>", views.UserNameReview.as_view()),
    path("", views.ReviewView.as_view()),
]

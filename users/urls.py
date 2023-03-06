from django.urls import path
from . import views

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("myprofile", views.UserProfileView.as_view()),
    path("user_password_change", views.UserPasswordView.as_view()),
    path("login", views.LoginView.as_view()),
    path("logout", views.LogoutView.as_view()),
    path("@<str:username>", views.UsernameView.as_view()),
]

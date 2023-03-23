from django.urls import path
from . import views

urlpatterns = [
    path("/signup", views.SignUpView.as_view()),
    path("/activate/<str:uidb64>/<str:token>", views.Activate.as_view()),
]

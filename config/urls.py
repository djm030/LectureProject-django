from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
<<<<<<< HEAD
    path("users/", include("users.urls")),
    path("lectures/", include("lectures.urls"))
=======
    path("api/v1/users/", include("users.urls")),
    path("api/v1/lectures/", include("lectures.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/videos/", include("videos.urls")),
    path("api/v1/reviews/", include("reviews.urls")),
    path("api/v1/qnas/", include("qnas.urls")),
>>>>>>> 8635767911e5135e624b04e9ca1cd276aa801718
]

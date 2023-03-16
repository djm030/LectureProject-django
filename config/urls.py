from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/lectures/", include("lectures.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/videos/", include("videos.urls")),
    path("api/v1/reviews/", include("reviews.urls")),
    path("api/v1/cart/", include("cart.urls")),
    path("api/v1/ledetaile/", include("ledetailes.urls")),
    path("api/v1/accounts/", include("accounts.urls")),
]

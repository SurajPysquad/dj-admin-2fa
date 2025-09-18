from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin-2fa/", include("dj_admin_2fa.urls")),
]

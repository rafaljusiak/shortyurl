from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from shortyurl.urls.api.viewsets import UrlViewSet

v1_router = routers.DefaultRouter()
v1_router.register("urls", UrlViewSet, basename="urls")

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "api/v1/",
        include(v1_router.urls),
        name="api-v1",
    ),
]

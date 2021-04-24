from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("it/", include("it.urls")),
    path('admin/', admin.site.urls),
]

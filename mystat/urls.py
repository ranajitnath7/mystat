from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin-test/', admin.site.urls),
]

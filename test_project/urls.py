"""This module contains main urls"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', include('test_app.urls'))
]

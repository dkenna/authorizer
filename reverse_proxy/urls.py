"""reverse_proxy URL Configuration
"""
from django.contrib import admin
from django.urls import path
from reverse_proxy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reverse_proxy),
]

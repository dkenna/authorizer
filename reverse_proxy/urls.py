"""reverse_proxy URL Configuration
"""
from django.urls import path
from reverse_proxy.views import reverse_proxy

urlpatterns = [
    path('', reverse_proxy),
]

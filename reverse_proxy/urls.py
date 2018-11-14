"""reverse_proxy URL Configuration
"""
from django.urls import path
from reverse_proxy.views import reverse_proxy
from django.conf.urls import include, url

urlpatterns = [
    url(r'^oidc/', include('mozilla_django_oidc.urls')),
    url(r'^', reverse_proxy),
]

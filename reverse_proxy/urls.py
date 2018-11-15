"""reverse_proxy URL Configuration
"""
from django.urls import path
from reverse_proxy.views import reverse_proxy,login_view,logout_view
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^login', login_view),
    url(r'^logout', logout_view),
    url(r'^oidc/', include('mozilla_django_oidc.urls')),
    path('admin/', admin.site.urls),
    #url(r'^', login),
    url(r'^', reverse_proxy),
]

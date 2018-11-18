"""authorizer URL Configuration
"""
from django.urls import path
from authorizer.views import reverse_proxy,login_view,logout_view
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^login', login_view),
    url(r'^logout', logout_view),
    url(r'^oidc/', include('mozilla_django_oidc.urls')),
    path('admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    #url(r'^', login),
    url(r'^', reverse_proxy),
]

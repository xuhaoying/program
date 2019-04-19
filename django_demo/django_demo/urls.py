"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^01-show/$', show_views),
    url(r'^login/$', login),
    url(r'^register/$', register),
    url(r'^02-url/(\d{4})/$', url_views),
    url(r'^03-url/(\d{4})/(\d{1,2})/(\d{1,2})/$', url_views_03),
    url(r'^04-url/(\S{2,})/(\d{1,2})/$', url_views_04),
]



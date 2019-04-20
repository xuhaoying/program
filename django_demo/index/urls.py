from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views),
    url(r'^index/$', index_views),
    url(r'^login/$', login),
    url(r'^register/$', register),
]

urlpatterns += [
    url(r'^temp01/$', temp01),
    url(r'^temp02/$', temp02),
    url(r'^temp03/$', temp03_static),
]




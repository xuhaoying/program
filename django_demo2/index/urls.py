from django.conf.urls import url ,include
from .views import *

urlpatterns = [
    url(r'01-parent/', parent_views),
    url(r'01-child/', child_views),
]
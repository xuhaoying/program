from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01-request/$', request_views),
    url(r'^02-get/$', get_views),
    url(r'^03-post/$', post_views),
    url(r'^04-register/$', register_views),
    url(r'^05-form/$', form_views),
    url(r'^06-savedb/$', save_db_views),
]

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01-request/$', request_views),
    url(r'^02-get/$', get_views),
    url(r'^03-post/$', post_views),
    url(r'^04-register/$', register_views),
    url(r'^05-form/$', form_views),
    url(r'^06-savedb/$', save_db_views),
    url(r'^07-login/$', login_views),
    url(r'^08-info/$', info_views),
]

urlpatterns = [
    url(r'^09-server/$', server09_views),
    url(r'^10-json/$', json_views),
    url(r'^11-json-user/$', json_users),
    url(r'^12-json-post/', ajax_post),
    url(r'^12-server/$', server12_views),
]


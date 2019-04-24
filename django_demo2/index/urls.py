from django.conf.urls import url ,include
from .views import *

urlpatterns = [
    url(r'01-parent/', parent_views),
    url(r'01-child/', child_views),
]

urlpatterns = [
    url(r'02-create/', create_views),
    url(r'02-createpub/', create_publisher),
    url(r'02-createbook/', create_book),
    url(r'03-retrieve/', retrieve_views),
    url(r'04-aggregate/', aggregate_views),
    url(r'04-annotate/', annotate_views),
    url(r'^05-queryall', query_all),
    url(r'^05-querybyid/(\d+)/$', query_by_id),
    url(r'^05-deletebyid/(\d+)/$', delete_by_id),
    url(r'^05-updatebyid/(\d+)/$', update_by_id),
    url(r'^06-addage/$', add_age),
    url(r'^07-queryor/$', query_or),
]

urlpatterns += [
    url(r'^08-oto/$', oto_views),
    url(r'^09-otm/$', otm_views),
]

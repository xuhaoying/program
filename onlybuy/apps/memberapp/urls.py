from django.urls import path, include
from .views import *

urlpattern = [
    path("product_detail/", product_details),
]


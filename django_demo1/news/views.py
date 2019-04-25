from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_views(response):
    return HttpResponse("这是 news 中的 index 页面")

def show_views(response):
    return HttpResponse("这是 news 中的 show 页面")
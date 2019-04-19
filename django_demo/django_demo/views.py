# In django, HttpResponse can respond to a piece of text in the client browser
from django.http import HttpResponse


def show_views(request):
    """
    View handlers that handle the business
    :param request:  The request object of this request encapsulates all the information in the request
    :return: The content of the response to the client
    """
    return HttpResponse("This is my first Django application.")

def login(request):
    return HttpResponse("这是登录页面")

def register(request):
    return HttpResponse("这是注册页面")

def url_views(request, param):
    return HttpResponse("传入的参数是{}".format(param))

def url_views_03(request, param1, param2, param3):
    return HttpResponse("生日: {} 年 {} 月 {} 日".format(param1, param2, param3))

def url_views_04(request, param1, param2):
    return HttpResponse("姓名: {} <br>年龄: {}岁".format(param1, param2))

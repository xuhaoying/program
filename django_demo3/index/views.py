from django.shortcuts import render
from django.http import HttpResponse
from .forms import *


# Create your views here.
def request_views(request):
    print(dir(request))
    request_str = """
    - request.scheme 请求协议 {} <br>
    - request.body 请求主体 {} <br>
    - request.method 请求方式  {} <br>
    - request.GET 获取以 GET 方式请求提交的数据  {} <br>
    - request.POST 获取以 POST 方式请求提交的数据  {} <br>
    - request.path 获取请求路径  {} <br>
    - request.get_full_path()  获取完整的请求路径  {} <br>
    - request.get_host()  获取请求的主机、域名  {} <br>
    - request.COOKIES  获取 cookie 中的数据  {} <br>        
    - request.session  获取 session 中的数据  {} <br>   
    - request.META  获取 请求消息头  {} <br>
    - request.META["HTTP_REFERER"]  获取请求源地址  {} <br>
    """.format(
        request.scheme, request.body, request.method, request.GET,
        request.POST, request.path, request.get_full_path(),
        request.get_host(), request.COOKIES, request.session,
        request.META, request.META.get('HTTP_REFERER'),
    )
    return HttpResponse(request_str)

def get_views(request):
    # 从地址栏输入 uname  和 uage 的参数
    uname = request.GET.get("uname")
    uage = request.GET.get("uage")
    print('uname', uname)
    print('uage', uage)
    return HttpResponse("""
    uname: {} <br>
    uage: {} <br>
    """.format(uname, uage))

def post_views(request):
    if request.method == 'GET':
        return render(request, '03-post.html')
    if request.method == 'POST':
        uname = request.POST.get("uname")
        uage = request.POST.get("uage")
        return HttpResponse(
            "uname: {}  <br>uage: {}".format(uname,uage))
    return HttpResponse("获取失败")

def register_views(request):
    if request.method == 'GET':
        return render(request, '04-register.html')
    name = request.POST.get("name")
    age = request.POST.get("age")  
    gender = request.POST.get("gender")
    hobby = request.POST.getlist('hobby')
    native_place = request.POST.get("native_place")
    ret_str = """
    name {}  <br>
    age {}  <br>
    gender {}  <br>
    hobby {}  <br>
    native_place {}  <br>
    """.format(name, age, gender, hobby, native_place)
    return HttpResponse(ret_str)

def form_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request, '05-form.html', locals())
    else:
        form = RemarkForm(request.POST)
        data = "None"
        if form.is_valid():  # 通过验证
            data = form.cleaned_data
        print(data)
        return HttpResponse("{}".format(data))

def save_db_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, '06-savedb.html', locals())
    else:
        form = RegisterForm(request.POST)
        data = "None"
        if form.is_valid():  # 通过验证
            data = form.cleaned_data
        print(data)
        return HttpResponse("{}".format(data))


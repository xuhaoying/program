import json
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
from .forms import *
from .models import *

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
        action = "/06-savedb/"
        return render(request, '06-savedb.html', locals())
    else:
        form = RegisterForm(request.POST)
        data = "None"
        if form.is_valid():  # 通过验证
            data = form.cleaned_data
            # 插入数据库
            user = Users(**data)
            user.save()
            return HttpResponse("插入数据库成功<br>{}".format(data))
        print(data)
        return HttpResponse("插入失败<br>{}".format(data))

def login_views(request):
    if request.method == 'GET':
        # 判断是否由保存的登录信息，如果有，则显示欢迎xxx
        uname = request.session.get('uname')
        print("session", uname)
        if uname:
            return HttpResponse("欢迎 {}".format(uname))

        uname = request.COOKIES.get('uname')
        print("cookie", uname)
        if uname:
            return HttpResponse("欢迎 {}".format(uname))
        # 没有则正常显示登录页面
        form = LoginForm()
        action = "/07-login/"
        return render(request, '06-savedb.html', locals())
    else:
        form = LoginForm(request.POST)

        resp = redirect("/07-login")  # 响应对象

        if form.is_valid():  # 通过验证
            data = form.cleaned_data
            # 去数据库中验证用户名和密码是否正确

            uname = data.get('uname')
            upwd = data.get('upwd')
            save_time = data.get('saveTime')
            user = Users.objects.filter(uname=uname, upwd=upwd)

            if user:
                # 保存 cookie 根据保存时长
                if save_time == '1':
                    max_age = 0
                elif save_time == '2':
                    max_age = 1 * 30 * 24 * 60 * 60
                elif save_time == '3':
                    max_age = 6 * 30 * 24 * 60 * 60
                elif save_time == '4':
                    max_age = 365 * 24 * 60 * 60

                resp.set_cookie('uname', uname, max_age=max_age)
                resp.set_cookie('upwd', upwd, max_age=max_age)

                request.session['uname'] = uname
                request.session['upwd'] = upwd
                print("request.session >> ", request.session)

                return resp

        return resp

def info_views(request):
    if request.method == 'GET':
        form = InfoForm()
        action = "/08-info/"
        return render(request, '06-savedb.html', locals())
    else:
        form = InfoForm(request.POST)
        data = "None"
        if form.is_valid():  # 通过验证
            data = form.cleaned_data
            print(data)
        print(data)
        return HttpResponse("{}".format(data))

def server09_views(request):
    uname = request.GET['uname']
    uage = request.GET['uage']
    print(uage, uname)
    return HttpResponse("这是09-server的响应内容<br> uname: {} <br>uage: {}".format(uname, uage))

def json_views(request):
    person = {
        "name": "Maria",
        "age": 18,
        "gender": "gril",
        "email": "maria@163.com",
    }
    personStr = json.dumps(person)
    return HttpResponse(personStr)

def json_users(request):
    users = Users.objects.all()
    jsonStr = serializers.serialize("json", users)
    return HttpResponse(jsonStr)

def ajax_post(request):
    return render(request, "12-ajax-post.html")

def server12_views(request):
    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd')
    print("uname", uname)
    print("upwd", upwd)
    return HttpResponse("uname: {} <br>uage:{}".format(uname, upwd))
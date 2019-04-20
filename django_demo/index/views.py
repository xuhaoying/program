from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index_views(response):
    return HttpResponse("这是 index 中的 index 页面")

def login(request):
    return HttpResponse("这是 index 中的登录页面")

def register(request):
    return HttpResponse("这是 index 中的注册页面")

def temp01(request):
    dic = {
        "name": "Maria",
        "age": 12,
        }
    t = loader.get_template("01temp.html")
    html = t.render(dic)
    return HttpResponse(html)

def temp02(request):
    
    name = "Tom"
    age = 18
    hobby = ["music", 'draw','computer']
    films = {
        "MSN": "美少女战士",
        "XMX": "巴拉巴拉小魔仙",
    }
    class Animal(object):
        name = "wang"
        def eat(self):
            return self.name + " is eating..."

    animal = Animal()
    animal.name = "duoduo"
    
    print(locals())
    return render(request, "01temp.html", locals())
    # return render_to_response("01temp.html", dic)

def temp03_static(request):
    return render(request, '03static.html')
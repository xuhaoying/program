from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Avg, Count, F, Q
from wsgiref.simple_server import ServerHandler

# Create your views here.
def parent_views(request):
    uname = 'Parent'
    return render(request, '01-parent.html', locals())

def child_views(request):
    uname = 'Child'
    return render(request, '01-child.html', locals())

def create_views(request):
    # Entry.objects.create()
    # au1 = Author.objects.create(
    #     name="Jerry", age=36, email="Jerry@163.com"
    # )

    # obj = Author(name="Amy")
    # obj.age = 39
    # obj.email = "Amy@163.com"
    
    dic = {
        "name": "Alice",
        "age": 18,
        "email": "Alice@163.com"
    }
    obj = Author(**dic)

    obj.save()
    print("ID: {}, 姓名: {}, 年龄: {}, 邮箱: {}, 是否激活: {}".format(
        obj.id, obj.name, obj.age, obj.email, obj.isActive
    ))
    return HttpResponse("增加数据成功")

def create_publisher(request):
    # dic = {
    #     "name":  
    #     "address": 
    #     "city":  
    #     "country":  
    #     "website":  
    # }
    # obj = Publisher(**dic)
    # obj,save()
    
    return HttpResponse("")

def create_book(request):
    return HttpResponse("")

def retrieve_views(request):
    # ret = Author.objects.all()
    # print("Author.objects", ret)
    # print("Author.objects type", type(ret))
    # for au in ret:
    #     print("au", au)

    # ret = Author.objects.values_list("name")
    # ret = Author.objects.filter(id=1, name="Maria")
    # ret = Author.objects.filter(age__gt=30)
    # ret = Author.objects.filter(name__startswith='A')
    ret = Author.objects.filter(email__contains='m')
    print(ret)
    return HttpResponse("查询成功")

def aggregate_views(request):
    ret = Author.objects.filter(age__gt=30
            ).aggregate(avgAge=Avg('age'), numPeople=Count('id'))
    print(ret)
    return HttpResponse("查询成功")


def annotate_views(request):
    ret = Author.objects.values('age').annotate(
        numPeople=Count('id'))
    print(ret)
    return HttpResponse("查询成功")

def query_all(request):
    authors = Author.objects.filter(isActive=True)
    print(authors)
    return render(request, '05queryall.html', locals())

def query_by_id(request, id):
    # get找不到会报错的
    author = Author.objects.get(id=id)
    return render(request, '05queryById.html', locals())

def delete_by_id(request, id):
    Author.objects.filter(id=id).update(isActive=False)
    return redirect("/05-queryall")

def update_by_id(request, id):
    Author.objects.filter(id=id).update(age=F('age')+1)
    return redirect("/05-queryall")

def add_age(request):
    Author.objects.all().update(age=F('age')+1)
    return HttpResponse("更改成功")

def query_or(request):
    authors = Author.objects.filter(Q(id=1)|Q(age__gt=45))
    print(authors)
    return HttpResponse("查询成功")

def oto_views(request):
    # 向wife 表中增加对象
    # 通过外键属性关联属性
    # wife = Wife()
    # wife.wname = "Mrs.Peter"
    # wife.wage = 18
    # wife.author_id = 2
    # wife.save()

    # author = Author.objects.get(id=5)
    # wife = Wife()
    # wife.wname = "Mrs.Amy"
    # wife.wage = 19
    # wife.author = author
    # wife.save()

    wife = Wife.objects.get(id=1)
    print("{}'s husband's name is {}.".format(
            wife.wname,  wife.author.name)
           )
    
    author = Author.objects.get(id=2)
    print("{}'s wife is {}.".format(
        author.name, author.wife.wname
    ))

    return HttpResponse("注册 wife 成功")

def otm_views(request):
    pub = Publisher.objects.get(id=3)
    print(pub.book_set.all())
    print(type(pub.book_set))
    print("object 类型", type(pub))
    return HttpResponse("查询数据成功")


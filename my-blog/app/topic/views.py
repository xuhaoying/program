"""
此处编写有关 topic 的路由和视图
"""
import os
import json
import datetime
from flask import render_template, request, session, redirect

from . import topic
from .. import db
from app.models import *


@topic.route("/")
def index():
    cates = Category.query.all()
    # 判断 session 中是否有登录信息, 有的话则取出对应的对象

    # 查询 topic 中前20条数据并放在首页中进行显示
    topics = Topic.query.limit(20).all()

    user = None
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template("index.html", cates=cates, user=user,
        topics=topics)

@topic.route("/list")
def list_category():
    # 查询 category 所有信息,
    id = request.args.get("id")
    # 点击类型去往 list?id=当前类型的 id
    # 到 /list 中接受id 的值, 并查询出 category_id 为指定id的文章信息并显示在 list.html中
    category = Category.query.filter_by(id=id).first()
    return render_template("list.html", id=id)

@topic.route("/release", methods=['GET', 'POST'])
def release():
    if request.method == 'GET':
        # 判断是否有用户登录
        if 'id' in session and 'loginname' in session:
            id = session['id']
            user = User.query.filter_by(ID=id).first()
            # 判断该用户是否有发表博客的权限
            print(user.is_author)
            if user.is_author:
            # 查询 category 中的所有信息, 发送到 release.html上 
                cates = Category.query.all()
                print(cates)
            # 已select 方式显示,提供给用户选择
                return render_template("release.html", cates=cates)
        # ,没有登录重定向回首页
        return redirect("/")
        
    else:
        topic = Topic()
        # 接受信息并插入回数据库 Topic中
        topic.title = request.form.get("author")
        topic.blogtype_id = request.form.get("list")
        topic.category_id = request.form.get("cate")
        topic.pub_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        topic.content = request.form.get("content")
        topic.user_id = session['id']
        topic.read_num = 0

        print(request.files)
        # 注意上传的图片
        if request.files.get('picture'):
            picture = request.files.get('picture')
            print(picture)
            # 得到文件的名称(获取扩展名)
            ext = picture.filename.split('.')[-1]
            # 获取当前时间： YYYYMMDDHHMMSSFFFFFF
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            # 将时间与扩展名拼接到一起， 组成新的文件名
            filename = ftime + '.' + ext
            # 使用完整路径上传
            # picture.save("/home/tarena/test/program/blog/test/flask_demo/static/upload" + filename)
            # 得到 app 的绝对路径, 向上两级文件夹下
            basedir = os.path.dirname(os.path.dirname(__file__))
            # print("basedir : " + basedir)
            # 拼接完整的保存路径
            upload_path = os.path.join(basedir, 'static/upload', filename)
            picture.save(upload_path)

            topic.images = os.path.join("upload", filename)

        db.session.add(topic)   

        print("title >> ", topic.title)
        print("pub_date >> ", topic.pub_date)
        print("read_num >> ", topic.read_num)
        print("content >> ", topic.content)
        print("images >> ", topic.images)
        print("blogtype_id >> ", topic.blogtype_id)
        print("category_id >> ", topic.category_id)
        print("user_id >> ", topic.user_id)

        # 将文件上传至 static/upload 目录下
        # picture.save('static/upload/' + filename)
        # 图片保存路径 /static/upload
        return render_template("release.html")


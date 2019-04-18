"""
此处编写有关 users 的路由和视图
"""

from flask import render_template, request, redirect, session

from . import users
from .. import db
from app.models import *


def login():
    if request.method == 'GET':
        # print(request.referrer)
        print(request.headers.get("Referer", '/'))
        url = request.headers.get("Referer", '/')
        session['url'] = url

        # 判断是否已经处于登录状态(去session中判断有没有 id loginname)
        if 'id' in session and 'loginname' in session:
            # 获取请求源地址,保存session 用于登录成功
            # 没有请求地址则将 '/' 存入 session
            # print(request.referrer)
            return redirect("/")
        return render_template("login.html")
    else:
        
        loginname =request.form.get('username')
        upwd =request.form.get('password')
        user = User.query.filter_by(loginname=loginname, upwd=upwd).first()
        if user:
            session['id'] = user.ID
            session['loginname'] = loginname
            # 登录成功, 返回登录前地址,如果没有则返回首页
            # print(request.headers.get("Referer", '/'))
            url = session['url']
            return redirect(url)
        # 登录失败, 返回登录页面
        return redirect("/login")





users.add_url_rule("/login", view_func=login, methods=['GET', 'POST'])




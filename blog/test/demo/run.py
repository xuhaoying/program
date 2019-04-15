from flask import Flask, make_response, request, render_template
from flask import session
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import json

app = Flask(__name__)
# 配置数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/ajax"
# 不追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 调试模式
app.config['DEBUG'] = True

# 配置数据库操作的自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SECRET_KEY'] = 'whatever'

db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(80), nullable=False, unique=True, index=True)
    upwd = db.Column(db.String(20), nullable=False)
    uphone = db.Column(db.String(20), unique=True) 
    uemail = db.Column(db.String(120),unique=True)



@app.route('/01setcookie')
def set_cookie():
    # 保存 名称为 username， 值为 Maria 的 cookie 到浏览器中
    # 保存时间 : 3年
    # 响应内容 保存 cookie 成功 
    # 使用 make_response() 构建响应对象
    resp = make_response("<h1>保存cookie成功</h1>")
    resp.set_cookie('username', 'Maria', 60*60*24*365*3)
    # 不设置时长， 则为会话期有效
    # resp.set_cookie('username', 'Maria')
    return resp

@app.route('/02getcookie')
def get_cookie():
    # cookies = request.cookies
    # print(cookies)

    # 取cookie的值
    if 'username' in request.cookies:
        username = request.cookies.get('username')
        print('username:', username)
    return '获取cookie成功'

@app.route('/03deletecookie')
def delete_cookie():
    resp = make_response('删除cookie成功')
    resp.delete_cookie('username')
    return resp

@app.route('/login', methods=['GET', 'POST'])
def login():
    # 记住密码登录 username password
    # 验证用户名和密码， 如果成功则认为登陆成功
    # 登录成功之后判断是否记住密码， 如果记住密码，保存进cookie
    # 再次访问登录地址，判断cookie中是否有用户名和密码，
    #  如果有，显示xx欢迎回来, 如果没有，显示登录页面

    # 登录成功后将用户名和密码保存进session （只在会话期有效）
    # 如果勾选记住密码， 将用户名和密码保存进cookie中
    # 访问登录页面，判断session中是否有登录信息， 
    # 如果session中有信息，直接响应欢迎xxx回来
    # 如果session中没有登录信息， 判断cookie中是否有登录信息
    # cookie中有登录信息时，将信息取出保存进session，再响应欢迎xx回来
    # 如果cookie中也没有登录信息，重新登录
    if request.method == 'GET':
        # 判断session中是否有登录信息， 
        username = session.get('username', '')
        password = session.get('password', '')
        if username == 'admin' and password == 'admin':
            return '欢迎 {} 回来'.format(username)
        # session中没有登录信息， 再判断cookie中是否有登录信息
        username = request.cookies.get('username', '')
        password = request.cookies.get('password', '')
        if username == 'admin' and password == 'admin':
            session['username'] = username
            session['password'] = password
            return '欢迎 {} 回来'.format(username)
        # 不对的话，删除cookie中与登录相关的数据
        resp = make_response(render_template('login.html'))
        resp.delete_cookie('username')
        resp.delete_cookie('password')
        return resp
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        # 判断是否登录成功
        if username == 'admin' and password == 'admin':
            resp = make_response('登录成功')
            # 将用户名和密码保存进session中
            session['username'] = username
            session['password'] = password
            if 'isRemember' in request.form:
                # 设置记住密码 将用户名和密码保存进cookie中
                max_age = 60*60*24*365
                resp.set_cookie('username', username, max_age)
                resp.set_cookie('password', password, max_age)
            return resp
        return '''
        <script>
        alert('用户名或密码错误');
        location.href='/login';
        </script>
        '''
    
@app.route('/setsession')
def setsession():
    session['username'] = 'maria'
    session['password'] = '123456'
    return "保存session成功"

@app.route('/getsession')
def getsession():
    # 建议获取session值之前先做判断
    username = session.get('username', '')
    password = session.get('password', '')
    print('username', username)
    print('password', password)
    return '获取session成功'

@app.route('/01-ajax-get')
def ajax_get():
    return render_template('/01-ajax-get.html')

@app.route('/01server')
def server01():
    return "这是使用 AJAX 方式发送的请求"

@app.route('/loginuser')
def user_login():
    return render_template('loginuser.html')
   

@app.route('/02server')
def server02():
    uphone = request.args.get('uphone')
    ret = User.query.filter_by(uphone=uphone).first()
    if ret:
        # 返回状态值，而不是具体存在的文本
        return '0'  # "该电话号码已被注册"
    return '1'  # "可以注册"

@app.route("/03post")
def post_views():
    return render_template("03post.html")

@app.route("/03server01",  methods=['POST'])
def server03_01():
    # 接受前端传递的数据
    uname = request.form.get('uname')
    upwd = request.form.get('upwd')
    # 将数据再响应给前端
    return """
    注册成功 <br>
    用户名： {} <br>
    密码： {} <br>
    """.format(uname, upwd)

@app.route("/03server02",  methods=['POST'])
def server03_02():
    # 接受前端传递的数据
    uname = request.form.get('uname')
    upwd = request.form.get('upwd')
    # 将数据再响应给前端
    return """
    注册成功 <br>
    用户名： {} <br>
    密码： {} <br>
    """.format(uname, upwd)

@app.route('/03server03', methods=['POST'])
def server03_03():
    user = User()
    uphone = request.form.get('uphone')
    uname = request.form.get('uname')
    upwd = request.form.get('upwd')
    uemail = request.form.get('uemail')

    user.uphone  = uphone 
    user.uname  = uname 
    user.upwd  = upwd 
    user.uemail  = uemail 
    try:
        db.session.add(user)
        return '1'
    except Exception as e:
        print(e)
        return '0'

@app.route('/04users')
def users():
    return render_template('04users.html')

@app.route('/04server')
def server04():
    users = User.query.all()
    print(users)
    return "ok"

@app.route('/jsview')
def js_view():
    return render_template("JavaScriptObject.html")


if __name__ == '__main__':
    # app.run(debug=True) 
    manager.run()
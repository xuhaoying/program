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

    # 创建一个方法，负责将本类的属性们转换为字典
    def to_dict(self):
        dic = {
            'id': self.id,
            'uname': self.uname,
            'upwd': self.upwd,
            'uphone': self.uphone,
            'uemail': self.uemail ,
        }
        return dic


class Province(db.Model):
    __tablename__ = 'province'
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(32), unique=True)
    citys = db.relationship(
                'City', 
                backref='subprovince', 
                lazy='dynamic'
                )
    
    def to_dict(self):
        dic = {
            "id": self.id,
            "pname": self.pname,
        }
        return dic


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(32), unique=True)
    # 外键
    pid = db.Column(db.Integer, db.ForeignKey('province.id'))

    def to_dict(self):
        dic = {
            "id": self.id,
            "cname": self.cname,
            "pid": self.pid,
        }
        return dic


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
    # 使用 Python 字典表示 json 的单个对象
    obj = {
    "uname": "Maria",
    "uage": 30,
    "gender": "Female"
    }
    

    obj = [
        {
        "uname": "Maria",
        "uage": 30,
        "gender": "Female"
        },
        {
        "uname": "Alice",
        "uage": 26,
        "gender": "Female"
        },
        {
        "uname": "Tom",
        "uage": 38,
        "gender": "Male"
        },
    ]
    print("转换之前, obj数据类型 ", type(obj))
    jsonStr = json.dumps(obj)
    print("转换之前, jsonStr数据类型 ", type(jsonStr))

    return jsonStr

@app.route('/05json')
def sql_json():
    users = User.query.all()
    user_list = [
        {
        "uname": user.uname,
        "upwd": user.upwd,
        "uphone": user.uphone,
        "uemail": user.uemail,
        } for user in users
        ]

    user_list = [
        user.to_dict() for user in users
    ]

    return json.dumps(user_list)

@app.route('/05temp')
def temp05():
    return render_template('05json.html')

@app.route("/citys")
def citys():
    return render_template("citys.html")

@app.route("/getPro")
def get_pro():
    # 获取province中所有的数据并封装成JSON返回
    province = Province.query.all()
    proList = [
        pro.to_dict() for pro in province
    ]
    return json.dumps(proList)

@app.route("/getCity")
def get_city():
    # 接受前段传递过来的省份 id
    pid = request.args.get('pid')
    # 根据 pid 获取对应的城市信息
    citys = City.query.filter_by(pid=pid).all()
    cityList = [
        city.to_dict() for city in citys
    ]
    return json.dumps(cityList)

@app.route('/07temp',methods=['GET', 'POST'])
def temp07():
    # 接受参数
    # uname = request.args.get("uname")
    # uage = request.args.get("uage")
    
    uname = request.form.get("uname")
    uage = request.form.get("uage")

    print("uname >> ", uname)
    print("uage >> ", uage)
    return render_template("07temp.html")

@app.route('/07load')
def load07():
    return render_template('07load.html')

@app.route("/08jqget")
def jq_get():
    return render_template("08jqget.html")

@app.route("/08server")
def server08():
    # 接收前段传递过来的参数 uname
    uname = request.args.get("uname")
    # 根据 uname 的值去数据库中查询对应的 users 的信息
    user = User.query.filter_by(uname=uname).first()
    if user:
        return json.dumps(user.to_dict())
    dic = {
        "errMsg": "查无此人"
        }
    return json.dumps(dic)

@app.route("/getemail")
def get_email():
    return render_template("exc-email.html")

@app.route("/exc-server")
def exc_server():
    # 接收前段传递过来的参数 kw
    # 根据 kw 去 uemail 中模糊查询
    # 将查询出的内容构建成 JSON 串再响应
    kw = request.args.get("kw")
    users = User.query.filter(User.uemail.like("%{}%".format(kw))).all()
    if users:
        users_lst = [user.to_dict() for user in users]
        return json.dumps(users_lst)
    dic = {
        "errMsg": "暂无数据"
    }
    return json.dumps(dic)

@app.route("/10ajax")
def ajax10():
    return render_template("10ajax.html")

@app.route("/10server")
def server10():
    users = User.query.all()
    usersList = [user.to_dict() for user in users]
    return json.dumps(usersList)

@app.route("/11cross")
def corss_vies():
    return render_template("11cross.html")

@app.route("/11server")
def server11():
    return "这是11cross.html"

@app.route("/12js")
def js12_view():
    return "console.log('这是/12js的响应内容')"

@app.route("/13cross")
def cross13():
    return render_template("13cross.html")

@app.route("/13server")
def server13():
    # 接受前段传入的callback 表示
    cb = request.args.get("callback")
    users = User.query.all()
    # userList = [user.to_dict() for user in users]
    userList = [user.to_dict() for user in users]
    userStr = json.dumps(userList)
    return "{}({})".format(cb, userStr)

@app.route("/14cross")
def cross14():
    return render_template("14cross.html")

@app.route("/14server")
def server14():
    cb = request.args.get("callback")
    # 航班信息
    dic = {
        "fightNo":  "CA768",
        "from":  "Beijing",
        "to":  "Shanghai" ,
        "time":  "15:15",
    }
    data = json.dumps(dic)
    return "{}({})".format(cb, data)
    # return data


if __name__ == '__main__':
    # app.run(debug=True) 
    manager.run()
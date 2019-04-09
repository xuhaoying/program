import datetime
import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
# 配置数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/blog"
# 不追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 调试模式
app.config['DEBUG'] = True

db = SQLAlchemy(app)


# 将app交给Manager管理， 由Manager启动程序
manager = Manager(app)
# 创建Migrate对象,指定关联的app和db
migrate = Migrate(app, db)
# 为manager增加做数据库迁移的子命令
# 为数据库增加db子命令, 该命令具体操作由MigrateCommand提供
manager.add_command('db', MigrateCommand)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    url = db.Column(db.String(120), nullable=True)
    password = db.Column(db.String(100), nullable=False)

# db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list/')
def list():
    return render_template('list.html')

@app.route('/listcopy/')
def listcopy():
    return render_template('list_copy.html')

@app.route('/info/')
def info():
    return render_template('info.html')

@app.route('/infocopy/')
def infocopy():
    return render_template('info_copy.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == "POST":
        # 登录验证
        # 接受用户名和密码
        username = request.form.get("username")
        password = request.form.get("password")
        # 从数据库中验证, 并给出提示
        # 查找
        user = db.session.query(Users).filter_by(
            username=username, password=password).first()
        if user:
            return "<script>alert('登录成功');</script>"

        return '''<script>
                alert('用户名或密码错误'); 
                location.href='/login';
                </script>'''
        # return '''
        # username: {}
        # password: {}
        # '''.format(username, password)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        url = request.form.get("url")
        password = request.form.get("password")
        return '''
        username: {}
        email: {}
        url: {}
        password: {}
        '''.format(username, email, url, password)

@app.route('/release', methods=['GET', 'POST'])
def release():
    if request.method == 'GET':
        return render_template('release.html')
    else:
        # 获取数据
        author = request.form['author']
        list = request.form['list']
        print("author >> ", author)
        print("list >> ", list)
        # 有文件上传
        if request.files:
            picture = request.files['picutre']
            ext = picture.filename.split('.')[-1]
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            filename = ftime + '.' + ext
            basedir = os.path.dirname(__file__)
            upload_path = os.path.join(basedir, 'static/upload', filename)
            picture.save(upload_path)
            print("upload_path >> ", upload_path)

        content = request.form['content']
        print("content >> ", content)
        return '''发布博客成功'''






if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0", port=19480)
    manager.run()



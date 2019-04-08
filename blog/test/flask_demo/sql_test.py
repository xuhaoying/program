from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 导入pymsql, 并且将其伪装成MySQLdb
# import pymysql
# pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 配置数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/flask"
# 不追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 调试模式
app.config['DEBUG'] = True

# 在程序中， 通过db操作数据库
db = SQLAlchemy(app)
print(db)


# 将app交给Manager管理， 由Manager启动程序
manager = Manager(app)

# 创建Migrate对象,指定关联的app和db
migrate = Migrate(app, db)
# 为manager增加做数据库迁移的子命令
# 为数据库增加db子命令, 该命令具体操作由MigrateCommand提供
manager.add_command('db', MigrateCommand)


# 创建实体类 Users, 映射到数据库中users表
# id  主键 自增长
# username  长度为80的字符串， 不允许为空， 唯一， 加索引
# age  整数， 允许为空
# email 长度为120的字符串， 必须唯一
class Users(db.Model):
    __tablename__ = "users" 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True, index=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120),unique=True)
    # 增加一个字段， isActive, 
    isActive = db.Column(db.Boolean, default=True)


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True, nullable=False)


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), unique=True, index=True)


# 删除所有的表, 不要用
# db.drop_all()
# 将Users类映射到数据库（表不存在时才会创建）
db.create_all()


@app.route('/')
def index():
    return "这是首页"

if __name__ == "__main__":
    # app.run(debug=True, port=8888)
    
    # 指定调试模式 debug=True, app.config['DEBUG'] = True
    # 指定端口 python3 run.py runserver --port xxxx
    # 制定启动的IP地址 python3 run.py runserver --host 0.0.0.0
    # python3 run.py runserver --host 0.0.0.0 --port xxxx

    # 使用manager 启动服务
    manager.run()


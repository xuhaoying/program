from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import or_, func
import math

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

# 配置数据库操作的自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# 在程序中， 通过db操作数据库
db = SQLAlchemy(app)

# 将app交给Manager管理， 由Manager启动程序
manager = Manager(app)

# 创建Migrate对象,指定关联的app和db
migrate = Migrate(app, db)
# 为manager增加做数据库迁移的子命令
# 为数据库增加db子命令, 该命令具体操作由MigrateCommand提供
manager.add_command('db', MigrateCommand)

class Users(db.Model):
    __tablename__ = "users" 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True, index=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120),unique=True)
    # 增加一个字段， isActive, 
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<Users: '{}'>".format(self.username)

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
    # 增加一个外键列 cid, 引用自course表的主键 id
    cid = db.Column(db.Integer, db.ForeignKey('course.id'))


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), unique=True, index=True)
    # 想通过teachers的属性来得到对应的所有teacher信息
    # 增加关联属性和反向引用关系属性, relationship只影响类,没有对数据库进行映射
    teachers = db.relationship(
                Teacher, backref='course', lazy='dynamic'
                )


@app.route('/01regtea', methods=['GET', 'POST'])
def regtea01():
    '''
    注册老师
    下拉列表（要将所有的课程读取出来放在里面）
    '''
    if request.method == 'GET':
        # 所有的课程
        courses = Course.query.all()
        # print(course)
        return render_template('01regtea.html', courses=courses)
    else:
        tea = Teacher()
        tea.tname = request.form.get('tname')
        tea.tage = request.form.get('tage')
        tea.cid = request.form.get('course')
        db.session.add(tea)
        # print('tname', tea.tname)
        # print('tage', tea.tage)
        # print('cid', tea.cid)
        # print(tea.course)
        return '''<script>
        alert('注册老师成功');
        location.href="/01regtea";
        </script>'''

@app.route('/02query')
def query02():
    '''
    根据课程查询对应的老师， 课程为下拉列表
    第一项为请选择， 剩余的内容要从数据库中读取出来
    当下拉列表的内容发生改变时， 则读取出对应课程的所有老师， 显示在下方
    如果下拉列表中选择的是请选择，则读取全部内容

    下拉列表选项发生更改时， 发生的改变为 onchange()
    '''
    courses = Course.query.all()
    
    id = int(request.args.get('id', '0'))
    # print(id)
    course = Course.query.filter_by(id=id).first()
    # print(course)
    if not course:
        teachers = Teacher.query.all()
    else:
        teachers = course.teachers.all()
    return render_template(
        '02query.html', 
        courses=courses, teachers=teachers)



if __name__ == '__main__':
    manager.run()  # db migrate  # db upgrade




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
    wife = db.relationship(
        'Wife', backref='user', uselist=False
        )

    def __repr__(self):
        return "<Users: '{}'>".format(self.username)


class Wife(db.Model):
    __tablename__ = 'wife'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True, index=True)
    age = db.Column(db.Integer, nullable=True)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True, nullable=False)
    # 学生对应的课程们


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)
    # 增加一个外键列 cid, 引用自course表的主键 id
    cid = db.Column(db.Integer, db.ForeignKey('course.id'))
    students = db.relationship(
        'Student', lazy='dynamic',
        backref = db.backref('teachers', lazy='dynamic'),
        secondary='student_teacher'
        )


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), unique=True, index=True)
    # 想通过teachers的属性来得到对应的所有teacher信息
    # 增加关联属性和反向引用关系属性, relationship只影响类,没有对数据库进行映射
    teachers = db.relationship(
                'Teacher', backref='course', lazy='dynamic'
                )
    # 课程对应的老师们
    students = db.relationship(
                'Student', lazy='dynamic', # 针对Course类中的students属性的延迟加载
                backref=db.backref(
                    'courses', lazy='dynamic'),  # 针对Student类中的courses属性的延迟加载
                secondary="student_course"  # 指定第三张关联表
                )


class StudentCourse(db.Model):
    __tablename__ = 'student_course'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer,  db.ForeignKey('course.id'))


class StudentTeacher(db.Model):
    __tablename__ = 'student_teacher'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    teacher_id = db.Column(db.Integer,  db.ForeignKey('teacher.id'))


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
        tea.cid = request.form.get('cid')
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
    
    cid = int(request.args.get('cid', '0'))
    # print(id)
    # 查询对应cid的课程信息
    course = Course.query.filter_by(id=cid).first()
    # print(course)
    # 如果没有找到课程， 显示全部老师信息
    if not course:
        teachers = Teacher.query.all()
    else:
        teachers = course.teachers.all()
    return render_template(
        '02query.html', 
        courses=courses, teachers=teachers, cid=cid)

@app.route('/03regwife', methods=['GET', 'POST'])
def reg_wife():
    if request.method == 'GET':
        return render_template('03refwife.html')
    else:
        wife = Wife()
        user = Users()
        user.username = request.form.get('uname')
        user.age = request.form.get('uage')
        user.email = request.form.get('email')
        user.isActive = False
        if 'isActive' in request.form:
            user.isActive = True
        # wife.name = request.form.get('wname')
        # wife.age = request.form.get('wage')
        # wife.user = user
        db.session.add(user)
        # db.session.add(wife)
        # 允许通过wife.uid 关联对应user的id
        # 允许通过wife.user 关联对应的user对象
        return render_template('03refwife.html')

@app.route('/04query')
def query04():
    '''
    查询wife对应的user
    下拉菜单显示user, 然后下面显示user信息和妻子信息
    '''
    users = Users.query.all()
    # uid = int(request.args.get('uid', '0'))
    # print('wife', wife.name)
    # print('user', user.username)
    return render_template('04query.html', users=users)

@app.route('/05select', methods=['GET', 'POST'])
def select05():
    '''
    注册wife， 提供下拉单身汉供选择
    '''
    if request.method == 'GET':
        users = Users.query.all()
        bachelors = []  # 没有wife的单身汉们
        for user in users:
            if not user.wife:
                bachelors.append(user)
        return render_template('05select.html', bachelors=bachelors)
    else:
        wife = Wife()
        wife.name = request.form.get('wname')
        wife.age = request.form.get('wage')
        wife.uid = request.form.get('uid')
        # 检查uid是否已经存在， 在页面没有刷新的时候，可能已经另一个被选择了
        user = Wife.query.filter_by(uid=wife.uid).first()
        if user:
            return '''
            <script>
            alert("该男子已被选走了,请重新选择");
            location.href="/05select";
            </script>
            '''
        db.session.add(wife)
        return '''
            <script>
            alert("注册成功！");
            location.href = '/05select';
            </script>
            '''

@app.route('/joinquery')
def join_query():
    '''
    查询id为1的学生所选择的课程， 以及选择该课程的学生们
    '''
    stu = Student.query.filter_by(id=1).first()
    print(stu.courses.all())
    for course in stu.courses.all():
        print(course)
        print(course.students.all())
    
    return "查询成功"

@app.route('/insertsc')
def insert_sc():
    '''
    向第三张表中插入关联数据
    关联属性/反向引用关系属性都提供了
    append()方法用于关联两张表中的数据到第三张表中

    查询id为1的学员信息
    查询Python基础的课程信息
    '''
    stu = Student.query.filter_by(id=1).first()
    cou = Course.query.filter_by(id=1).first()
    # 方案一 通过stu属性courses将cou关联
    stu.courses.append(cou)
    # 方案二 通过cou属性students将stu关联

    return "插入数据成功"

@app.route('/regstu', methods=['GET', 'POST'])
def reg_student():
    if request.method == 'GET':
        courses = Course.query.all()
        return render_template('06regstu.html', courses=courses)
    else:
        # 接受请求提交的数据
        # 创建Student类的对象, 赋值并插入到数据库
        stu = Student()
        stu.sname = request.form.get('sname')
        stu.sage = request.form.get('sage')
        stu.isActive = False
        if 'isActive' in request.form:
            stu.isActive = True
        courses = request.form.getlist('courses')
        # print(courses)
        # 向第三张关联表中插入数据
        stu.courses = Course.query.filter(Course.id.in_(courses)).all()
        print(stu.courses)
        # for cid in courses:
        #     course = Course.query.filter_by(id=cid).first()
        #     stu.courses.append(course)
        db.session.add(stu)

        return '''
        <script>
        alert("注册成功!");
        location.href = '/regstu';
        </script>
        '''

@app.route('/addtea')
def add_tea():
    '''
    # 学生，选择课程， 同时选择课程所对应的老师， 选择老师
    学生根据所选择的课程选择老师
    '''
    return render_template('08addtea.html')

@app.route('/queryall')
def queryall():
    '''
    查询学生选修的课程及对应的老师
    '''
    students = Student.query.all()
    return render_template('07queryall.html', students=students)

if __name__ == '__main__':
    manager.run()  # db migrate  # db upgrade




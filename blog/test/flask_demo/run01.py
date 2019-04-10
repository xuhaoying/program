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
# print(db)

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


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), unique=True, index=True)


# 删除所有的表, 不要用
# db.drop_all()
# 将Users类映射到数据库（表不存在时才会创建）
# db.create_all()


@app.route('/')
def index():
    return "这是首页"

@app.route('/01add')
def add_views():
    # 创建Users的对象
    user = Users()
    user.username = 'Xiao'
    user.age = 17
    user.email = 'Xiao@163.com'
    # 将Users对象保存回数据库并提交
    db.session.add(user)
    # 非查询操作一定要提交
    # db.session.commit()
    return 'Users创建成功'

@app.route('/addstudent')
def add_student():
    student = Student()
    student.sname = 'Peter'
    student.sage = 8
    db.session.add(student)
    return "add student sucessfully."

@app.route('/addteacher')
def add_teacher():
    teacher = Teacher()
    teacher.tname = 'Mr.Xi'
    teacher.tage = 42
    db.session.add(teacher)
    return "add teacher sucessfully."

@app.route('/02register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('02register.html')
    else:
        user = Users()
        # 接受模板传递过来的数据
        # 将数据构建成 Users 的对象
        user.username = request.form['username']
        user.age = request.form['age']
        user.email = request.form['email']
        user.isActive = False
        if 'isActive' in request.form:
            user.isActive = True
        # 将对象保存回数据库
        db.session.add(user)
        return "注册新用户成功"

@app.route('/02add')
def add02():
    for i in range(1000):
        user = Users()
        # 接受模板传递过来的数据
        # 将数据构建成 Users 的对象
        user.username = 'test_{}'.format(i)
        user.age = 8
        user.email = user.username + '@163.com' 
        # 将对象保存回数据库
        db.session.add(user)
    return "添加用户成功"

@app.route('/03query')
def query_views():
    '''查询Users类中所有数据'''
    query = db.session.query(Users)
    users = query.all()
    # print(users)
    for user in users:
        # user 表示的就是users列表中的每一条数据(Users对象))
        print("姓名: {}, 年龄: {}, 邮箱: {}".format(user.username, user.age, user.email))
    return "查询数据成功"

@app.route('/03queryall')
def queryall():
    '''查询Users类中所有数据并在页面上显示'''
    query = db.session.query(Users)
    users = query.all()
    return render_template("03queryall.html", users=users)

@app.route('/04query')
def query01():
    # users = db.session.query(Users).filter(Users.age>40).filter(Users.isActive==True).all()
    # users = db.session.query(Users).filter(or_(Users.age>40, Users.isActive==True)).all()
    # users = db.session.query(Users).filter(Users.age.in_([30, 33])).all()
    # users = db.session.query(Users).filter(Users.age.between(20,40)).all()
    # users = db.session.query(Users).filter_by(id=1).first()
    # users = db.session.query(Users).order_by('age desc').all()
    users = db.session.query(Users).order_by("age desc, id").all()
    # users = db.session.query(func.sum(Users.age)).all()
    print(users)
    return "查询数据成功"

@app.route('/05query')
def query05(): 
    pageSize = 5
    page = int(request.args.get('page', '1'))
    # 跳过(page-1)*pageSize条数据再获取pageSize条数据
    ost = (page-1) * pageSize
    # 客户端向服务端要数据, 使用get请求
    # 判断是否有kw参数, 如果没有则为''
    kw = request.args.get('kw', '')
    if kw:
        users = db.session.query(Users).filter(
            or_(Users.username.like('%{}%'.format(kw)), 
            Users.email.like('%{}%'.format(kw))
            ))
    else:
        users = db.session.query(Users)
    if not users:
        users = db.session.query(Users)
    # 计算尾页页码
    # 计算总记录数并将结果保存在totalCount中
    totalCount = len(users.all())

    users = users.offset(ost).limit(pageSize).all()
    # 通过totalCount和pageSize计算尾页, 向上取整
    lastPage = math.ceil(totalCount / pageSize)
    # 通过page计算上一页(prevPage)和下一页(nextPage)
    prevPage = 1
    if page > 1:
        prevPage = page - 1
    
    nextPage = lastPage
    if page < lastPage:
        nextPage = page + 1
    
    # print(page ,lastPage ,prevPage ,nextPage )
    return render_template('05query.html', users=users, kw=kw,
    page=page, lastPage=lastPage, prevPage=prevPage, nextPage=nextPage)

@app.route('/05page')
def page_views():
    # pageSize 表示每页显示的记录数量
    pageSize = 10
    # 接受前端传递过来的请求参数page, 表示想看的页数, 如果没有该参数, 则设置为1
    page = int(request.args.get('page', '1'))
    # 跳过(page-1)*pageSize条数据再获取pageSize条数据
    ost = (page-1) * pageSize
    users = db.session.query(Users).offset(ost).limit(pageSize).all()
    # 计算尾页页码
    # 计算总记录数并将结果保存在totalCount中
    totalCount = db.session.query(Users).count()
    # 通过totalCount和pageSize计算尾页, 向上取整
    lastPage = math.ceil(totalCount / pageSize)
    # 通过page计算上一页(prevPage)和下一页(nextPage)
    prevPage = 1
    if page > 1:
        prevPage = page - 1
    
    nextPage = lastPage
    if page < lastPage:
        nextPage = page + 1

    return render_template("05page.html", 
    page=page, users=users, lastPage=lastPage, prevPage=prevPage, nextPage=nextPage)

@app.route('/06aggregate')
def aggregate_views():
    # result = db.session.query(func.sum(Users.age)).all()
    # print(result)
    # print('age sum : %d' % result[0])
    # result = db.session.query(func.avg(Users.age),
    # func.max(Users.age), func.min(Users.age)
    # ).all()
    # print(result)
    # result = result[0]
    # avg_age,  max_age, min_age = result[0], result[1], result[2]
    
    # print("avg_age: %.2f" % avg_age)
    # print("max_age: %d" % max_age)
    # print("min_age: %d" % min_age)
    # 查询USers实体中, 按isActive分组后每组的人数
    # db.session.query(查询列, 聚合列).group_by('属性名').all()
    # result = db.session.query(
    #     Users.isActive, func.count(Users.isActive)
    #     ).group_by(Users.isActive).all()

    result = db.session.query(
        Users.isActive, func.avg(Users.age)
    ).group_by(Users.isActive).having(func.avg(Users.age)>18).all()
    print(result)
    return "聚合查询成功"

@app.route('/07aggregate')
def aggregate07():
    # 查询Users总年龄
    res = db.session.query(func.sum(Users.age)).all()
    print("总年龄:", res)
    # 查询Users总人数
    res = db.session.query(func.count(Users.id)).all()
    print("总人数: ",res)
    # 查询Users 年龄大于18岁的 人的平均年龄
    res = db.session.query(func.avg(Users.age)
        ).filter(Users.age>18).all()
    print("查询Users 年龄大于18岁的 人的平均年龄", res)
    # 按 isActive 分组后 组内人数大于2人的(组, 人数)
    res = db.session.query(
        Users.isActive, func.count(Users.id)
        ).group_by(Users.isActive
        ).having(func.count(Users.id)>2).all()
    print(" 按 isActive 分组后 组内人数大于2人的(组, 人数)", res)
    # 年龄大于18的人按isActive分组后, 组内人数大于2人的信息
    res = db.session.query(
        Users.isActive, func.count(Users.id)
        ).filter(Users.age>18).group_by(Users.isActive
        ).having(func.count(Users.id)>2).all()
    print(" 年龄大于18的人按isActive分组后, 组内人数大于2人的信息", res)
    return "分组聚合查询成功"

@app.route('/08update', methods=['GET', 'POST'])
def update08():
    '''
    GET 请求, 接受传递过来的id, 并查询数据显示在08update.html上
    POST 请求. 接受要修改的数据并更新回数据库
    '''
    if request.method == 'GET':
        id = int(request.args.get('id', '0'))
        user = Users.query.filter_by(id=id).first()
        return render_template('08update.html', user=user)
    else:
        id = int(request.form.get('id', '0'))
        user = Users.query.filter_by(id=id).first()    
        user.username = request.form['username']
        user.age = request.form['age']
        user.email = request.form['email']
        user.isActive = False
        if 'isActive' in request.form:
            user.isActive = True
        db.session.add(user)
        return '''<script>
                alert('修改成功'); 
                location.href='/05query';
                </script>'''

@app.route('/09delete')
def delete09():
    id = int(request.args.get('id', '0'))
    user = Users.query.filter_by(id=id).first()
    db.session.delete(user)
    return redirect('/05query')
    


if __name__ == "__main__":
    # app.run(debug=True, port=8888)
    
    # 指定调试模式 debug=True, app.config['DEBUG'] = True
    # 指定端口 python3 run.py runserver --port xxxx
    # 制定启动的IP地址 python3 run.py runserver --host 0.0.0.0
    # python3 run.py runserver --host 0.0.0.0 --port xxxx

    # 使用manager 启动服务
    manager.run()


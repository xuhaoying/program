"""
当前程序的初始化操作

主要工作:
1. 构建 Flask 应用实例及各种配置
2. 创建 SQLAlchemy 的实例
3. ...
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 声明 SQLAlchemy 的实例 - db
db = SQLAlchemy()

def create_app():
    # 创建 flask 应用 -app
    app = Flask(__name__)
    # 为 app 设置各种配置
    # 配置启动模式为调式模式
    app.config['DEBUG'] = True
    # 配置数据库的连接信息
    app.config['SQLALCHEMY_DATABASE_URI'
            ] = "mysql+pymysql://root:123456@localhost:3306/blognew"
    # 配置数据库的自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    # 配置数据库的信号追踪
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 配置session 所需要的 secret_key
    app.config['SECRET_KEY'] = "justWriteSth"

    # 关联 db 和 app
    db.init_app(app)

    # 将 topic 蓝图程序与 app 进行关联
    from .topic import topic as topic_blueprint
    app.register_blueprint(topic_blueprint)
    
    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)
    
    # 返回 app
    return app





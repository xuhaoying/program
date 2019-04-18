"""
启动和项目管理的相关操作代码
"""

import datetime
import os

from flask import render_template, request
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import *

# 创建 app
app = create_app()
# 创建 manager 对象用于管理 app
manager = Manager(app)
# 创建 migrate 对象用于关联要管理的 app 和 db
migrate = Migrate(app, db)
# 创建 manager 对象增加 db 的迁移指令
manager.add_command('db', MigrateCommand)






if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0", port=19480)
    manager.run()



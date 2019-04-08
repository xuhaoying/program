import datetime
import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/01file', methods=['GET', 'POST'])
def file_views():
    if request.method == 'GET':
        return render_template('01file.html')
    else:
        # 获取前端传递过来的文件
        picture = request.files['picture']
        # 得到文件的名称(获取扩展名)
        ext = picture.filename.split('.')[-1]
        # 获取当前时间： YYYYMMDDHHMMSSFFFFFF
        ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        # 将时间与扩展名拼接到一起， 组成新的文件名
        filename = ftime + '.' + ext
        # 使用完整路径上传
        # picture.save("/home/tarena/test/program/blog/test/flask_demo/static/upload" + filename)
        # 得到当前文件所在文件夹的绝对路径
        basedir = os.path.dirname(__file__)
        # print("basedir : " + basedir)
        # 拼接完整的保存路径
        upload_path = os.path.join(basedir, 'static/upload', filename)
        picture.save(upload_path)

        # 将文件上传至 static/upload 目录下
        # picture.save('static/upload/' + filename)
        return "头像上传成功"


if __name__ == '__main__':
    app.run()
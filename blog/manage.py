import datetime
import os
from flask import Flask, render_template, request

app = Flask(__name__)

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
        username = request.form.get("username")
        password = request.form.get("password")
        return '''
        username: {}
        password: {}
        '''.format(username, password)

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
    app.run(debug=True, host="0.0.0.0", port=19480)

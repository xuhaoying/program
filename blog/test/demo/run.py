from flask import Flask, make_response, request, render_template
from flask import session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'whatever'

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

@app.route('/01xml')
def xml01():
    return render_template('01xml.html')




if __name__ == '__main__':
    app.run(debug=True)
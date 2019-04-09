from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/<int:num>')
@app.route('/index/<int:num>')
def index(num=None):
    if num is not None:
        return "<h2>您当前要看的页数为第{}页</h2>".format(num)
    return "<h1>Welcome!</h1>"

@app.route('/calc/<int:num1>/<int:num2>')
def calc(num1, num2):
    ret = "{} + {} = {}<br/>".format(num1, num2, num1+num2)
    ret += "{} - {} = {}<br/>".format(num1, num2, num1-num2)
    ret += "{} * {} = {}<br/>".format(num1, num2, num1*num2)
    ret += "{} / {} = {}<br/>".format(num1, num2, num1/num2)
    ret += "{} // {} = {}<br/>".format(num1, num2, num1//num2)
    ret += "{} % {} = {}<br/>".format(num1, num2, num1%num2)
    
    return ret


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

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



if __name__ == '__main__':
    app.run(debug=True)

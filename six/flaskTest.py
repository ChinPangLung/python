# pip install flask
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def home():
    return '<h1>home</h1>'


@app.route('/signin', methods=['get'])
def singin_from():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['post'])
def singin():
    # 需要从requests对象中读取from表单数据
    print('==========')
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>hello admin</h3>'
    return '<h1>Bad username or password</h1>'


if __name__ == '__main__':
    app.run(port=9999)

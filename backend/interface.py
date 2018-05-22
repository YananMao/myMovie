from flask import Flask
from flask import request
from flask import jsonify
import douban

# print(douban.init())
app = Flask(__name__)
movies = douban.init()
@app.route('/', methods=['GET', 'POST'])
def home():
    # movies = douban.init()
    return jsonify(movies)

# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''

# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username']=='admin' and request.form['password']=='password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
    # print(1)
from flask import Flask,request,render_template

app = Flask(__name__)  #Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。在大多数程序中，Python 的 __name__ 变量就是所需的值。

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html');
@app.route("/user/<name>",methods=['POST','GET'])
def user(name):
    return "<h1>Hello,%s!</h1>" %name
@app.route("/login",methods=['GET'])
def form():
    return render_template("login.html")

@app.route("/login",methods=['POST'])
def login():
    # 需要从request对象读取表单内容：
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='123456':

     return render_template("index.html",message="欢迎"+username);
    else:
     return render_template("login.html",message="密码或者账号错误",username = username)
if __name__ == '__main__':
    app.run(debug=True)


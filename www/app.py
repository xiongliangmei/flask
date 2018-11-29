from flask import Flask,request,render_template

app = Flask(__name__)  #Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。在大多数程序中，Python 的 __name__ 变量就是所需的值。

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html');
@app.route("/user/<name>",methods=['POST','GET'])
def user(name):
    return "<h1>Hello,%s!</h1>" %name
if __name__ == '__main__':
    app.run(debug=True)


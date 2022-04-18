# -*- coding: utf-8 -*-
# author lby
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/index")
def index():
    return "<h1>hello world</h1>"


"""
动态url路由，restful，/put/user/zhangsan
"""
@app.route("/test/<name>")
def test(name):
    return name + "!!!!"


@app.route("/index1.h")
def index1():
    # 返回模板下的html
    return render_template("pages/index.html")


@app.route("/index2.h")
def index2():
    # 返回静态资源下的html，我们使用这种方式
    return send_from_directory("static","pages/index.html")


# 启动项目之后，加载的是当前启动函数所在文件夹下的所有资源
if __name__ == "__main__":
    app.run(debug=True)
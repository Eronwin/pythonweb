# -*- coding: utf-8 -*-
# author lby
import json

from flask import Blueprint, request, send_from_directory

from db import db_handler
from exts import db

"""
创建蓝图对象
参数1，蓝图点
"""
user = Blueprint("user", __name__)


"""
路由的method，http的请求方法，post、get、put、delete。。。。
"""
@user.route("/index", methods=["GET", "POST"])
def index():
    return "user的index"


@user.route("/test")
def test():
    return "user的test"


# 路由伪装html，伪装链接
@user.route("/index.html")
def index_html():
    return send_from_directory("static","pages/index.html")


@user.route("/add", methods=["GET", "POST"])
def add():
    """
    提前url的请求参数
    localhost:5000/user/add?username=zhan&age=11
    参数都在request.args
    """
    # username = request.args.get("username")
    # age = request.args.get("age")
    #
    # print(username + ", " + age)
    # print(dict(request.args))

    """
    提前form表单的请求参数
    未来做项目基本上全部使用ajax请求，请求参数一般使用json对象
    提前ajax请求参数，使用request.form
    """
    # name = request.form["name"]
    # age = request.form["age"]
    #
    # print(name + ", " + age)

    """
    接收其他客户端传递参数，json、xml。。。。
    request.data接收
    request.data本身是一个字符串
    目前演示是传递的json，所以request.data就是json字符串
    """
    print(request.data)
    json_obj = json.loads(request.data)  # json字符串转json对象
    name = json_obj["name"]
    age = json_obj["age"]
    print(name + ", " + age)

    return "user的index"


@user.route("/select", methods=["GET", "POST"])
def select():
    sql = "select * from user where id = 1"
    res = db.session.execute(sql).fetchone()  # 查询单条
    print(res)

    sql = "select * from user where id > 1"
    res = db.session.execute(sql).fetchall()  # 查询多条
    print(res)

    sql = "select * from user where id = :id"
    params = {"id": 2}
    # res = db.session.execute(sql, params).fetchone()  # 查询单条
    res = db_handler.select(sql, params, "one")
    print(res)

    return "ok"


@user.route("/write", methods=["GET", "POST"])
def write():
    sql = "insert into user (name,age) values (:name,:age)"
    params = {
        "name": "小红",
        "age": 15
    }

    # 增删改都是使用这种方式
    # db.session.execute(sql, params)
    # db.session.commit()  # 提交事务

    # db_handler.execute(sql, params)

    sqls = [
            {"sql": "insert into user(name) values (:name)", "params": {"name": "lisi1"}},
            {"sql": "insert into user(name) values (:name)", "params": {"name": "lisi2"}},
            {"sql": "insert into user(name) values (:name)", "params": {"name": "lisi3"}}
            ]
    db_handler.execute_many(sqls)

    return "ok"
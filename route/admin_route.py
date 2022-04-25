

from flask import Blueprint,send_from_directory,request,session,jsonify
from util import Response
from core import admin_core

admin= Blueprint("admin",__name__)

@admin.route("/login.html")
def login_html():
    return send_from_directory("static","pages/login.html")



@admin.route("/index.html")
def index_html():
    return send_from_directory("static","pages/index.html")


@admin.route("/login",methods=["GET","POST"])
def Login():
    print(request.form["username"],request.form["password"])
    res = admin_core.login(request.form)
    if res.code == "200":
        session["current_user"]=res.data

    return jsonify(res.__dict__)


@admin.route("/add", methods=["GET", "POST"])
def add():
    res = admin_core.add(request.form)
    return res


@admin.route("/load/select", methods=["GET", "POST"])
def load_select():
    res = admin_core.load_select(request.form)
    return res

@admin.route("/list/user",methods=["GET","POST"])
def list_page():
    res=admin_core.list_page(request.form)
    return res
from flask import Blueprint,send_from_directory,request,session,jsonify

from core import role_core

role= Blueprint("role",__name__)

@role.route("/add",methods=["GET","POST"])
def add():
    print(request.form)
    res=role_core.add(request.form)
    return res

@role.route("/update", methods=["GET", "POST"])
def update():
    res = role_core.update(request.form)
    return res

@role.route("/list/page",methods=["GET","POST"])
def list_page():
    res=role_core.list_page(request.form)
    return res
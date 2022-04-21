

from flask import Blueprint,send_from_directory,request,session,jsonify

from core import menu_core

menu= Blueprint("menu",__name__)

@menu.route("/first/all",methods=["GET","POST"])
def  first_all():
    res=menu_core.first_all()
    # print("menu_core:",res.data)
    return res
    
@menu.route("/add",methods=["GET","POST"])
def add_menu():
    res=menu_core.add_menu(request.form)
    return res

@menu.route("/list/page",methods=["GET","POST"])
def list_page():
    res=menu_core.list_page(request.form)
    return res

@menu.route("/get/id", methods=["GET", "POST"])
def get_id():
    res = menu_core.get_id(request.form)
    return res


@menu.route("/update", methods=["GET", "POST"])
def update():
    res = menu_core.update(request.form)
    return res

@menu.route("/all",methods=["GET","POST"])
def all():
    res=menu_core.all()
    # print("menu_core:",res.data)
    return res
    
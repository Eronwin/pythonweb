
from flask import Blueprint,send_from_directory

admin= Blueprint("admin",__name__)

@admin.route("/login.html")
def login_html():
    return send_from_directory("static","pages/login.html")
@admin.route("/index.html")
def index_html():
    return send_from_directory("static","pages/index.html")
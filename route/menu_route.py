# -*- coding: utf-8 -*-
# author lby
from flask import Blueprint

menu = Blueprint("menu", __name__)


@menu.route("/index")
def index():
    return "menu的index"
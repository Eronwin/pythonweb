# -*- coding: utf-8 -*-
# author lby
import os

from flask import Blueprint, request

from core import video_info_core

video_info = Blueprint("video_info", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__)).replace("route", "")


@video_info.route("/add", methods=["GET", "POST"])
def add():
    # 除了上传文件指定 普通参数使用request.form
    params = dict(request.form)
    # 上传文件提前
    file = request.files.get("v_pic")

    params["file"] = file
    params["BASE_DIR"] = BASE_DIR

    res = video_info_core.add(params)
    return res

@video_info.route("/list/page", methods=["GET", "POST"])
def list_page():
    res = video_info_core.list_page(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    return res
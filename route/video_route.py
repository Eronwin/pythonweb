
import os
from uuid import uuid4

from flask import Blueprint, send_from_directory, request, send_file

from core import video_core

video = Blueprint("video", __name__)


@video.route("/index.html")
def index_html():
    return send_from_directory("static","index.html")


@video.route("/type/id", methods=["GET", "POST"])
def type_id():
    res = video_core.type_id(request.form)
    return res


@video.route("/pic/<pic>")
def pic_path(pic):
    print(pic)
    return send_file(pic)


BASE_DIR = os.path.dirname(os.path.abspath(__file__)).replace("route", "")


# 上传影音文件
@video.route("/receive_audio", methods=["POST"])
def receive_audio():
    file = request.files.get("audio")
    if file:
        filename = "%s.m4a" % uuid4()
        filepath = os.path.join(BASE_DIR, "data", filename)
        file.save(filepath)
        print(filepath)
        return {"code": 200, "filename": filename}
    return {"code": 201, "msg": "上传失败"}


# 加载影音文件
@video.route("/get_audio/<filename>")
def get_audio(filename):
    print(os.path.join(BASE_DIR, "data", filename))
    return send_file(os.path.join(BASE_DIR, "data", filename))

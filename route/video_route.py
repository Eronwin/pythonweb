
import os

from flask import Blueprint, request
import json
from core import video_core

video = Blueprint("video", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__)).replace("route", "")

@video.route("/add", methods=["GET", "POST"])
def add():

    params = dict(request.form)
    file = request.files.get("v_pic")

    params["files"] = []

    v_code = params["v_code"]
    v_name = params["v_name"]

    # 最后一集
    last_episode_num = video_core.last_episode_num(params)
    print(type(last_episode_num))
    print(type(last_episode_num.data))

    episode_num = int(json.loads(last_episode_num.data)["episode_num"])

    # 遍历上传文件的文件名集合
    for filename in request.files:
        file = request.files.get(filename)  # 根据文件名拿上传文件
        if file:
            episode_num += 1  # 集数+1
            path = os.path.join(BASE_DIR, "data", v_code + "&" + v_name + "第" + episode_num.__str__() + "集&" + file.filename)
            file.save(path)  # 保存到硬盘
            params["files"].append({
                "path": path,
                "episode_num": episode_num
            })

    res = video_core.add(params)

    return res


# 视频的列表video_lib，操作只做删除
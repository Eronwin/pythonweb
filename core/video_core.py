
from core.base_core import service
from db import video_db


@service
def last_episode_num(params={}):
    data = video_db.last_episode_num(params)

    if not data:
        data = {"episode_num": 0}

    return data


@service
def add(params={}):
    video_db.add(params)
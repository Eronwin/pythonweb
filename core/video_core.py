from core.base_core import service
from db import video_db


@service
def type_id(params={}):
    return video_db.type_id(params)
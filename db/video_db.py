
from db import db_handler


def type_id(params={}):
    sql = "SELECT * FROM video_info WHERE video_type_id = :video_type_id ORDER BY id DESC LIMIT 6"
    return db_handler.select(sql, params)
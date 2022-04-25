
from db import admin_db
from models.message_model import Message
from models.js_grid_data import JsGridData
from flask import jsonify


from core.base_core import service
def login(params={}):
    user = admin_db.login(params)
    res = Message()
    if user:
        res.success()
        res.data=user
    else:
        res.failed()
    return res

@service
def add(params={}):
    admin_db.add(params)


# 列表、修改、删除


@service
def load_select(params={}):
    return admin_db.load_select(params)


def list_page(params={}):
    # print("params:",params)
    grid_data = JsGridData(params)


    data = admin_db.page_list(grid_data.__dict__)

    itemsCount = admin_db.conut(grid_data.__dict__)

    grid_data.data = data
    grid_data.itemsCount = itemsCount
    # print("grid_data:",grid_data.__dict__)
    return jsonify(grid_data.__dict__)
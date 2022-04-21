from core.base_core import service
from db import role_db
from flask import jsonify
from models.js_grid_data import JsGridData
@service
def add(params={}):
    role_db.add(params)

@service
def list_page(params={}):
    grid_data = JsGridData(params)


    data = role_db.page_list(grid_data.__dict__)

    itemsCount = role_db.conut(grid_data.__dict__)

    grid_data.data = data
    grid_data.itemsCount = itemsCount


    return grid_data

@service
def get_id(params={}):
    # 1、根据id查询role
    role = role_db.get_id(params)

    # 2、根据role_code查询role_menu
    role_menus = role_db.role_menus(role)

    data = {
        "role": role,
        "role_menus": role_menus
    }

    return data


@service
def update(params={}):
    role_db.update(params)

@service
def del_id(params={}):
    role_db.del_id(params)


@service
def all():
    return role_db.all()
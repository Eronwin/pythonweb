

from core.base_core import service
from models.js_grid_data import JsGridData
from models.message_model import Message
from db import menu_db
from flask import jsonify

def first_all():
    first_menu=jsonify(menu_db.first_all())
    # print("first_menu:",type(first_menu))
    return first_menu

@service
def add_menu(params={}):
    menu_db.add_menu(params)
    
def list_page(params={}):
    # print("params:",params)
    grid_data = JsGridData(params)


    data = menu_db.page_list(grid_data.__dict__)

    itemsCount = menu_db.conut(grid_data.__dict__)

    grid_data.data = data
    grid_data.itemsCount = itemsCount
    # print("grid_data:",grid_data.__dict__)
    return jsonify(grid_data.__dict__)

@service
def get_id(params={}):
    return menu_db.get_id(params)


@service
def update(params={}):
    menu_db.update(params)

@service
def all(params={}):
   return  menu_db.all(params)
@service
def del_id(params={}):
    menu_db.del_id(params)


@service
def left(user={}):

    first_menus = []

    left_menus = []

    if user["username"] == "admin":
        first_menus = menu_db.first_all()
    else:
        first_menus = menu_db.first_menus_username(user)

    for first_menu in first_menus:
        user["parent_id"] = first_menu["id"]
        second_menus = menu_db.second_menus_username(user)
        left_menus.append({
            "first_menu": first_menu,
            "second_menus": second_menus
        })

    data = {
        "code": "200",
        "left_menus": left_menus
    }

    return data
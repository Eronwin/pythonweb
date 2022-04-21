

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
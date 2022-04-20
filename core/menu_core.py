

from models.js_grid_data import JsGridData
from models.message_model import Message
from db import menu_db
from flask import jsonify

def first_all():
    first_menu=jsonify(menu_db.first_all())
    # print("first_menu:",type(first_menu))
    return first_menu

def add_menu(parms={}):
    print("parms:",parms)
    res = Message()
    try:
        menu_db.add_menu(parms)
        res.success()
       
    except:
        res.failed()
    return jsonify(res.__dict__)

def list_page(parms={}):
    # print("parms:",parms)
    grid_data = JsGridData(parms)
    data = menu_db.page_list(grid_data.__dict__)
    itemsCount = menu_db.conut()
    grid_data.data = data
    grid_data.itemsCount = itemsCount
    # print("grid_data:",grid_data.__dict__)
    return jsonify(grid_data.__dict__)

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

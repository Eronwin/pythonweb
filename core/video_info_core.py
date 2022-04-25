
import os
import uuid

from core.base_core import service
from db import video_info_db
from models.js_grid_data import JsGridData


@service
def add(params={}):
    v_code = uuid.uuid1().__str__()
    params["v_code"] = v_code
    file = params["file"]

    if file:
        filepath = os.path.join(params["BASE_DIR"], "pic", v_code + "&" + file.filename)
        file.save(filepath)
        params["v_pic"] = filepath

    video_info_db.add(params)


@service
def list_page(params={}):
    # 把route传递来的request.form给JsGridData
    grid_data = JsGridData(params)

    """
    JSGrid的与后台的返回数据格式有要求，json对象
    {
        "data": 查询的数据集合,  # 表格展示数据
        "itemsCount": 你的数据的总条数   #  计算页码
    }
    """

    # 1、查询的数据集合
    data = video_info_db.page_list(grid_data.__dict__)  # 分页数据集合

    # 2、数据的总条数
    itemsCount = video_info_db.count(grid_data.__dict__)

    grid_data.data = data
    grid_data.itemsCount = itemsCount

    return grid_data


# 视频信息列表上的修改和删除
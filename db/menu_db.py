from db import db_handler

def first_all():

    sql = "select * from menu where menu_level = '1'"
    first_menu = db_handler.select(sql)
    return first_menu


def add_menu(parms={}):

    sql = """
    INSERT INTO menu
    (menu_code,menu_name,menu_url,menu_level,parent_id,sort)
    VALUES
    (:menu_code,:menu_name,:menu_url,:menu_level,:parent_id,:sort)
    """
    db_handler.execute(sql, parms)

    

def page_list(parms={}):
    sql="select * from menu limit :offset,:pageSize"
    
    menus=db_handler.select(sql,parms)
    return menus

def conut():
    sql="select count(id) from menu"
    data=db_handler.select(sql,fecth="one")
    return int(data["conut"])
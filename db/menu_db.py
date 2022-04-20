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
    # sql=f"""
    # select m.*,p.menu_name parent_menu_name from menu m
    # left join menu pm on m.parent_id=pm.id
    # where m.menu_name like '%%{parms['search']}%%'
    # order by m.parent_id,m.sort
    # limit :offset,:pageSize
    # """
    menus=db_handler.select(sql,parms)
    return menus

def conut(parms={}):
    sql="select count(id) from menu"
    # sql=f"select count(id) from menu where menu_name like '%%{parms['search']}%%'"
    data=db_handler.select(sql,fecth="one")
    return int(data["count(id)"])
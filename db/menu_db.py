from db import db_handler

def first_all():

    sql = "select * from menu where menu_level = '1'"
    first_menu = db_handler.select(sql)
    return first_menu


def add_menu(params={}):

    sql = """
    INSERT INTO menu
    (menu_code,menu_name,menu_url,menu_level,parent_id,sort)
    VALUES
    (:menu_code,:menu_name,:menu_url,:menu_level,:parent_id,:sort)
    """
    db_handler.execute(sql, params)

    

def page_list(params={}):
    # sql="select * from menu limit :offset,:pageSize"
    sql=f"""
    select m.*,pm.menu_name parent_menu_name from menu m
    left join menu pm on m.parent_id=pm.id
    where m.menu_name like '%%{params['search']}%%'
    order by m.parent_id,m.sort
    limit :offset,:pageSize
    """
    menus=db_handler.select(sql,params)
    return menus

def conut(params={}):
    # sql="select count(id) from menu"
    sql=f"select count(id) from menu where menu_name like '%%{params['search']}%%'"
    data=db_handler.select(sql,fecth="one")
    return int(data["count(id)"])

def get_id(params={}):
    sql = "select * from menu where id = :id"
    data=db_handler.select(sql, params, fecth="one")
    print("get_id:",data)
    return data


def update(params={}):
    sql = """
        UPDATE menu
        SET menu_code = :menu_code,
         menu_name = :menu_name,
         menu_url = :menu_url,
         menu_level = :menu_level,
         parent_id = :parent_id,
         sort = :sort
        WHERE
            id = :id
        """
    db_handler.execute(sql, params)
def all(params={}):
    sql = "select * from menu"
    data=db_handler.select(sql)
    return data
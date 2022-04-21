from db import db_handler


def add(params={}):
    sqls=[]
    role_sql="insert into role(role_code,role_name) values(:role_code,:role_name)"
    sqls.append({
        "sql":role_sql,
        "params":params
    })


    role_menu_sql="insert into role_menu(role_code,menu_code) values(:role_code,:menu_code)"
    codes=params["codes"].split(",")

    for menu_code in codes:
        role_menu_params={
            "role_code":params["role_code"],
            "menu_code":menu_code
        }
        sqls.append({
            "sql":role_menu_sql,
            "params":role_menu_params
        })
    db_handler.execute_many(sqls)


def page_list(params={}):
    # sql="select * from menu limit :offset,:pageSize"
    sql=f"""
    select * from role
    where role_name like '%%{params['search']}%%'
    limit :offset,:pageSize
    """
    menus=db_handler.select(sql,params)
    return menus

def conut(params={}):
    # sql="select count(id) from menu"
    sql=f"select count(id) from role where role_name like '%%{params['search']}%%'"
    data=db_handler.select(sql,fecth="one")
    return int(data["count(id)"])

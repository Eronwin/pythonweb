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
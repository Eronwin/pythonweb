
from db import db_handler

def login(params={}):
    sql = "select * from admin where username = :username and password = :password"
    user = db_handler.select(sql,params,fecth="one")
    return user


def add(params={}):
    sqls = []
    admin_sql = "INSERT INTO admin (username,password,real_name,job_no) VALUES (:username,:password,:real_name,:job_no)"
    sqls.append({
        "sql": admin_sql,
        "params": params
    })
    admin_role_sql = "INSERT INTO admin_role (username,role_code) VALUES (:username,:role_code)"
    sqls.append({
        "sql": admin_role_sql,
        "params": params
    })
    db_handler.execute_many(sqls)


def load_select(params={}):
    sql = f"select * from {params['tab_name']}"
    return db_handler.select(sql)


def page_list(params={}):
    # sql="select * from menu limit :offset,:pageSize"
    sql=f"""
    select * from admin ad
    left join admin_role ar on ad.username = ar.username
    left join role ro on ro.role_code= ar.role_code
    where ad.username like '%%{params['search']}%%'
    limit :offset,:pageSize
    """
    menus=db_handler.select(sql,params)

    for x in menus:
        print(x)
    return menus

def conut(params={}):
    # sql="select count(id) from menu"
    sql=f"select count(id) from admin where username like '%%{params['search']}%%'"
    data=db_handler.select(sql,fecth="one")
    return int(data["count(id)"])
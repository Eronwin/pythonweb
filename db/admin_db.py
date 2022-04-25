
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
    select ad.*,ro.role_name role_name from admin ad
    left join admin_role ar on ad.username = ar.username
    left join role ro on ro.role_code= ar.role_code
    where ad.username like '%%{params['search']}%%'
    limit :offset,:pageSize
    """
    # sql=f"""
    # select * from admin ad
    # where ad.username like '%%{params['search']}%%'
    # limit :offset,:pageSize
    # """
    menus=db_handler.select(sql,params)
    return menus

def conut(params={}):
    # sql="select count(id) from menu"
    sql=f"select count(id) from admin where username like '%%{params['search']}%%'"
    data=db_handler.select(sql,fecth="one")
    return int(data["count(id)"])


def get_id(params={}):
    sql = """
    select ad.*,ar.role_code role_code from admin ad
    left join admin_role ar on ad.username = ar.username
    where ad.id = :id
    """
    data=db_handler.select(sql, params, fecth="one")
   
    return data


def update(params={}):
    sql1= "UPDATE admin SET username = :username,password = :password,real_name = :real_name,job_no = :job_no, WHERE id = :id "
    sqls =[]
    sqls.append({
        "sql":sql1,
        "params":params
    })
    sql2= "UPDATE admin_role SET role_code = :role_code WHERE username = :username"
    sqls.append({
        "sql":sql2,
        "params":params
    })
    res=db_handler.execute_many(sqls)
    print(res)


def del_id(params={}):
    sql = "DELETE FROM admin WHERE id = :id"
    db_handler.execute(sql, params)
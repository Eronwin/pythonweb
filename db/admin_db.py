
from db import db_handler

def login(params={}):
    sql = "select * from admin where username = :username and password = :password"
    user = db_handler.select(sql,params,fecth="one")
    return user
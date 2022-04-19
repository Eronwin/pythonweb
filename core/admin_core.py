import imp
from db import admin_db
from models.message_model import Message

def login(params={}):
    user = admin_db.login(params)
    res = Message()
    if user:
        res.success()
        res.data=user
    else:
        res.failed()
    return res
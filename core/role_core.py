from core.base_core import service
from db import role_db

@service
def add(params={}):
    role_db.add(params)
    
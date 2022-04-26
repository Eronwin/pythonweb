from functools import wraps

from flask import jsonify

from models.message_model import Message


def service(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        res = Message("200", "success")
        try:
            res = fn(*args, **kwargs)
            if res is None: 
                res = Message("200", "success")
        except Exception as e:
            res.failed()
            print(e)

        try:
            res_json = jsonify(res)
        except TypeError as e:
            res_json = jsonify(res.__dict__)

        return res_json

    return wrapper
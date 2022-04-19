
import json
from tkinter.messagebox import NO
def HttpResponse(code,msg,data):
    return json.dumps({"code":code,"msg":msg,"data":data})

def Success(data=None):
    return HttpResponse(200,"ok",data)
def Fail(data=None):
    return HttpResponse(400,"failed",data)

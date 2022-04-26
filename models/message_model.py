
class Message:
    code = ""
    msg = ""
    data = {}

    def __init__(self,code="",msg=""):
        self.code=code
        self.msg=msg
    def success(self,code="200",msg="success"):
        self.code = code
        self.msg = msg
    def failed(self,code="403",msg="Forbidden"):
        self.code = code
        self.msg = msg
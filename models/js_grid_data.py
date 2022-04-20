
class JsGridData:
    pageIndex = 0
    pageSize = 0
    offset=0
    data = []
    itemsCount = 0
    # search=""
    def __init__(self,parms={}):
        self.pageIndex =int(parms["pageIndex"])
        self.pageSize = int(parms["pageSize"])
        # self.search=int(parms["search"])
        self.offset = self.pageSize * (self.pageIndex - 1)
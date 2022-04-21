
class JsGridData:
    pageIndex = 0
    pageSize = 0
    offset=0
    data = []
    itemsCount = 0
    search=""
    def __init__(self,params={}):
        self.pageIndex =int(params["pageIndex"])
        self.pageSize = int(params["pageSize"])
        # self.search=int(params["search"])
        self.offset = self.pageSize * (self.pageIndex - 1)
        self.search=params["search"]
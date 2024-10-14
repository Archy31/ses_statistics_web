
class Sort_by:
    def __init__(self, column: str, order: str):
        self.column: str = column
        self.order: str = order
    

class Search:
    def __init__(self, column: str, value: str):
        self.column: str = column
        self.value: str = value
    


class Filter:
    def __init__(
        self, limit: int = 0, offset: int = 0, 
        sort_by: Sort_by = Sort_by(column="", order=""), 
        search: Search = Search(column="", value="")
        ):
        self.limit = limit
        self.offset = offset
        self.sort_by = sort_by
        self.search = search
      
    
    
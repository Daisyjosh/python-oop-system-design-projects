class RetailerRepository:
    def __init__(self):
        self.retailers = {}

    def add(self,r):
        self.retailers[r.retailer_id] = r
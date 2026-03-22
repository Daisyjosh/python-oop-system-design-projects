class OrderServices:
    def __init__(self):
        self.order = {}

    def add_order(self,o):
        self.order[o.id] = o
    
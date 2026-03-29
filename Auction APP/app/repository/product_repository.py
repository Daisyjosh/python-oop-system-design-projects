class ProductRepository:
    def __init__(self):
        self.products = {}

    def add(self,p):
        self.products[p.product_id] = p
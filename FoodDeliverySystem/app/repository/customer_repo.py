class CustomerRepo:
    def __init__(self):
        self.customer = {}

    def add(self,c):
        self.customer[c.customer_id] = c
        
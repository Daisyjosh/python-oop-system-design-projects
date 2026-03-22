class CustomerService:
    def __init__(self):
        self.customers = {}

    def add_customer(self,customer):
        self.customers[customer.id] = customer
    

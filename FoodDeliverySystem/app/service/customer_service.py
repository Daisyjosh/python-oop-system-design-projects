class CustomerService:
    def __init__(self,customer_repo):
        self.customer_repo = customer_repo

    def add_customer(self,c):
        self.customer_repo.add(c)
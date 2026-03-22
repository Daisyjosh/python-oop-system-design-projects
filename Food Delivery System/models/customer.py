from models.user import User
class Customer(User):
    def __init__(self,id,name,email,phone,address):
        super().__init__(id,name,email,phone)
        self.address = address
        self.cart = []

    def add_to_cart(self,item):
        self.cart.append(item)


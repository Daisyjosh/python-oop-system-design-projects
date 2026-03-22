class UserCartServices:
    def __init__(self):
        self.cart = {}
    
    def add_to_cart(self,c):
        self.cart[c.id] = c
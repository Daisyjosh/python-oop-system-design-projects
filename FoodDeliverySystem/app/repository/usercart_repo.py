class UserCartRepo:
    def __init__(self,menu_services):
        self.cart = {}
        self.menu_service = menu_services


    def add(self,c):
        self.cart[c.cart_id] = c

    def customer_cart(self,cart_id):
        print("\n ========== VIEW YOUR CART ==========\n")
        cart = self.cart[cart_id]
        cart_items = cart.cart_items
        total = 0
        for menu_id, qty in cart_items.items():
            item_name = self.menu_service.get_item_name(menu_id)
            price = self.menu_service.get_price(menu_id)
            amt = qty * float(price)
            total += amt
            print(f"Menu ID: {menu_id} | Item Name: {item_name} | Qty: {qty} | Price: {amt}")
        print(f"========= TOTAL BILL: {total} ========== ")

    def get_cart_items(self,cart_id):
        cart_items = self.cart.get(cart_id).cart_items
        for menu_id, qty in cart_items.items():
            menu = self.menu_service.get_item_name(menu_id)
            price = self.menu_service.get_price(menu_id)
            print(f"Item: {menu} | Qty: {qty} | Price: {price} | Amount: {qty*price}")
            
        
                
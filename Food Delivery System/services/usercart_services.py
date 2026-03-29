class UserCartServices:
    def __init__(self):
        self.cart = {}
        self.menu_services = None
    
    def add_to_cart(self,c):
        self.cart[c.cart_id] = c

    def view_cart(self, cart_id):
        if cart_id not in self.cart:
            print("Cart not found")
            return

        if not self.menu_services:
            print("Menu service not initialized")
            return

        cart_items = self.cart[cart_id].cart_items
        total = 0

        for menu_id, qty in cart_items.items():
            m = self.menu_services.get_item(menu_id)

            if not m:
                print(f"Item with ID {menu_id} not found in menu")
                continue

            amount = m.price * qty
            total += int(amount)

            print(f"Item Name: {m.item_name} x {qty} = {amount}")

        print(f"\nTotal Bill: {total}")
    
    def find_cart_id(self,cust_id):
        customer_carts = [cid for cid, cobj in self.cart.items() if cobj.cust_id == cust_id]
        if not customer_carts:
            return None

        return max(customer_carts)
    
    




class OrderServices:
    def __init__(self,usercart_services):
        self.order = {}
        self.usercartservies = usercart_services

    def add_order(self,o):
        self.order[o.order_id] = o

    def find_order_id(self,cart_id):
        for oid,oobj in self.order.items():
            if oobj.cart_id == cart_id:
                return oid
        print("Order ID not found for this Cart ID")
        return None
    
    def get_user_orders(self,cust_id):
        user_orders = []

        for order_id, order in self.order.items():
            cart = self.usercartservies.cart.get(order.cart_id)

            if cart and cart.cust_id == cust_id:
                user_orders.append(order)

        return user_orders

    
class OrderRepo:
    def __init__(self,cart_repo):
        self.order = {}
        self.cart_repo = cart_repo

    def add(self,o):
        self.order[o.order_id] = o
        return o.order_id
    
    def get(self,cust_id):
        for oid, oobj in self.order.items():
            if oobj.cust_id == cust_id:
                print(f"Order ID: {oid}")
                print(f"Status: {oobj.status}")
                print(f"Order at: {oobj.created_at}")
                self.cart_repo.get_cart_items(oobj.cart_id)
                
                
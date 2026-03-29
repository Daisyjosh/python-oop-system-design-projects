from app.model.order import Order
class OrderService:
    def __init__(self,order_repo):
        self.order_repo = order_repo

    def place_order(self,cust_id,cart_id,dp_id,status,created_at):
        order_no = len(self.order_repo.order)+1
        order_id = "ORDER" + str(order_no)
        order = Order(order_id,cust_id,cart_id,dp_id,status,created_at)
        return self.order_repo.add(order)
    
    def get_orders(self,cust_id):
        self.order_repo.get(cust_id)

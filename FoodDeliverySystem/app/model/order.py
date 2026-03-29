class Order:
    def __init__(self,order_id,cust_id,cart_id,dp_id,status,created_at):
        self.order_id = order_id
        self.cust_id = cust_id
        self.cart_id = cart_id
        self.dp_id = dp_id
        self.status = status
        self.created_at = created_at
        
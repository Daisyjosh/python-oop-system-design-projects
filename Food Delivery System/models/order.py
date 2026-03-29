class Order:
    def __init__(self, order_id, cart_id, dp_id):
        self.order_id = order_id
        self.cart_id = cart_id
        self.dp_id = dp_id
        self.status = "Delivered"
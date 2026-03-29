class ReviewServices:
    def __init__(self,order_services):
        self.reviews = {}
        self.order_services = order_services

    def add_reviews(self,review):
        self.reviews[review.id] = review

    def view_reviews(self,user_id):
        print("Get Reviews...")
        order_ids = self.order_services.get_user_orders(user_id)
        print(order_ids)
        if not order_ids:
            print("No orders Found!!")
        for rid, robj in self.reviews.items():
            if robj.order_id in order_ids:
                print(f"Review ID: {rid} | Order ID: {robj.order_id} | Review On: {robj.type} | Your Comment: {robj.comment} | Your Rating: {robj.rating}")

        
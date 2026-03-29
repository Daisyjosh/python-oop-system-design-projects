class ReviewRepo:
    def __init__(self):
        self.review = {}
    
    def cust_add(self,cr):
        print("Reached Review")
        self.review[cr.crev_id] = cr


    def get(self,cust_id):
        for rid, robj in self.review.items():
            if robj.cust_id == cust_id:
                print(f"Review ID: {rid} | ON: {robj.rev_type} | Order ID: {robj.order_id} | Rating: {robj.rating} | Comment: {robj.comment} | Created At: {robj.created_at}")


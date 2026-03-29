from app.model.customer_review import CustomerReveiw
from app.model.dp_review import DPReveiw
class ReviewService:
    def __init__(self,review_repo):
        self.review_repo = review_repo

    def add_cust_review(self,cust_id,order_id,rev_type,rating,comment,created_at):
        crev_no = len(self.review_repo.review)+1
        crev_id = "CR" + str(crev_no)
        cr = CustomerReveiw(crev_id,cust_id,order_id,rev_type,rating,comment,created_at)
        self.review_repo.cust_add(cr)

    def add_dp_review(self,dp_id,order_id,rev_type,rating,comment,created_at):
        dprev_no = len(self.review_repo.review)+1
        dprev_id = "DPR" + str(dprev_no)
        dpr = DPReveiw(dprev_id,dp_id,order_id,rev_type,rating,comment,created_at)
        self.review_repo.dp_add(dpr)
    
    def get_reviews(self,cust_id):
        self.review_repo.get(cust_id)
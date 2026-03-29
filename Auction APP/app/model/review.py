class Review:
    def __init__(self,review_id,reviewer_id,product_id,comment,rating,created_at):
        self.review_id = review_id
        self.reviewer_id = reviewer_id
        self.product_id = product_id
        self.comment = comment
        self.rating = rating
        self.created_at = created_at

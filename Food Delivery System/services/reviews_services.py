class ReviewServices:
    def __init__(self):
        self.reviews = {}

    def add_reviews(self,review):
        self.reviews[review.id] = review
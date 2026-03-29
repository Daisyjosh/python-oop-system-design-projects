class RestaurantService:
    def __init__(self,rest_repo):
        self.rest_repo = rest_repo

    def add_restaurant(self,r):
        self.rest_repo.add(r)
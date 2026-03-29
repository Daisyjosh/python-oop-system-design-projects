class RestaurantRepo:
    def __init__(self):
        self.restaurant =  {}

    def add(self,r):
        self.restaurant[r.res_id] = r

    
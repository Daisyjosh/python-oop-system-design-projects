class RestaurantServices:
    def __init__(self):
        self.restaurants = {}
    
    def add_restaurant(self,r):
        self.restaurants[r.id] = r
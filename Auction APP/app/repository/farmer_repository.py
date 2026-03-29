class FarmerRepository:
    def __init__(self):
        self.farmers = {}


    def add(self,f):
        self.farmers[f.id] = f

    def get(self,farmer_id):
        self.farmers.get(farmer_id)
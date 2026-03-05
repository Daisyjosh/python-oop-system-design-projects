from models.vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self,vehicle_number):
        super().__init__(vehicle_number,"BIKE")
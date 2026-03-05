class Vehicle:
    def __init__(self,vehicle_number,vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

    
    def get_vehicle_number(self):
        return self.vehicle_number
    
    def get_vehicle_type(self):
        return self.vehicle_type
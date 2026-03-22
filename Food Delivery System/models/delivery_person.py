from models.user import User
class DeliveryPerson(User):
    def __init__(self,id,name,email,phone,address,vehicle_no):
        super().__init__(id,name,email,phone)
        self.address = address
        self.vehicle_no = vehicle_no
        self.available = True

        


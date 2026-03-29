from model.user import User

class Farmer(User):
    def __init__(self,farmer_id,user_id,name,email,phone,role,location,created_at):
        super().__init__(user_id,name,email,phone,role,location,created_at)
        self.farmer_id = farmer_id
from model.user import User

class Retailer(User):
    def __init__(self,retailer_id, user_id, name, email, phone, role, location, created_at):
        super().__init__(user_id, name, email, phone, role, location, created_at)
        self.retailer_id = retailer_id

        
from app.model.user import User
class Customer(User):
    def __init__(self,customer_id,user_id,user_name,email,phone,location,created_at):
        super().__init__(user_id,user_name,email,phone,location,created_at)
        self.customer_id = customer_id

    
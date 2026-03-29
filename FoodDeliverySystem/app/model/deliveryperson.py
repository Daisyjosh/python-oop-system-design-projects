from app.model.user import User
class DeliveryPerson(User):
    def __init__(self, dp_id,user_id, user_name, email, phone, location, created_at):
        super().__init__(user_id, user_name, email, phone, location, created_at)
        self.dp_id = dp_id
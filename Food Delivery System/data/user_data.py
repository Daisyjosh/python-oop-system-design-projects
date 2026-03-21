from models.user import User 
class UserData:
    def __init__(self):
        User = {}

    def add_user(self,user_id,user_name,user_email):
        self.User[user_id] = User(user_id,user_name,user_email)


class UserServices:
    def __init__(self):
        self.users={}

    def add_users(self,user):
        self.users[user.id] = user
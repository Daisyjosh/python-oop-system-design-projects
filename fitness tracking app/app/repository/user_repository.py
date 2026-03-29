class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, username, password):
        for u in self.users:
            if u.username == username and u.password == password:
                return u
        return None
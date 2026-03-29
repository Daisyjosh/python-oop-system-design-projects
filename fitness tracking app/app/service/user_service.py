from app.model.user import User

class UserService:
    def __init__(self, repo):
        self.repo = repo

    def register(self, username, password):
        user_id = "U" + str(len(self.repo.users) + 1)
        user = User(user_id, username, password)
        self.repo.add_user(user)
        return "User Registered"

    def login(self, username, password):
        return self.repo.get_user(username, password)
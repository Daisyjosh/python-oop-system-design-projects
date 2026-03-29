class UserRepository:
    def __init__(self):
        self.users = {}
    
    def add(self,u):
        self.users[u.id] = u

    def get(self,id):
        return self.users.get(id)
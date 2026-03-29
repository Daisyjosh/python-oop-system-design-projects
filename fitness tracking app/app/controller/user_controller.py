class UserController:
    def __init__(self, service):
        self.service = service

    def register(self, username, password):
        return self.service.register(username, password)

    def login(self, username, password):
        return self.service.login(username, password)
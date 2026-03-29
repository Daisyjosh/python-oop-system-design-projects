class GoalController:
    def __init__(self, service):
        self.service = service

    def set_goal(self, user_id, target):
        return self.service.set_goal(user_id, target)
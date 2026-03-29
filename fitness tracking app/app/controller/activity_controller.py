class ActivityController:
    def __init__(self, service):
        self.service = service

    def add_activity(self, user_id, activity_type, duration):
        return self.service.add_activity(user_id, activity_type, duration)

    def view_activities(self, user_id):
        return self.service.view_activities(user_id)
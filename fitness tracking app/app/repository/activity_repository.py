class ActivityRepository:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def get_user_activities(self, user_id):
        return [a for a in self.activities if a.user_id == user_id]
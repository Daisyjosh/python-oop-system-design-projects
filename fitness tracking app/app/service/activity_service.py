from app.model.activity import Activity

class ActivityService:
    def __init__(self, repo):
        self.repo = repo

    def add_activity(self, user_id, activity_type, duration):
        activity_id = "A" + str(len(self.repo.activities) + 1)
        activity = Activity(activity_id, user_id, activity_type, duration)
        self.repo.add_activity(activity)
        return "Activity Added"

    def view_activities(self, user_id):
        return self.repo.get_user_activities(user_id)
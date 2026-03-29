from app.model.goal import Goal

class GoalService:
    def __init__(self, repo):
        self.repo = repo

    def set_goal(self, user_id, target):
        goal_id = "G" + str(len(self.repo.goals) + 1)
        goal = Goal(goal_id, user_id, target)
        self.repo.add_goal(goal)
        return "Goal Set"
class GoalRepository:
    def __init__(self):
        self.goals = []

    def add_goal(self, goal):
        self.goals.append(goal)
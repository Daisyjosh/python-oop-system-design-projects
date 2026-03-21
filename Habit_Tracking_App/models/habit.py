class Habit:
    def __init__(self,user_id,habit_name,template_id,category_id,description,goal,frequency,habit_id = None,created_at = None):
        self.habit_id = habit_id
        self.user_id = user_id
        self.habit_name = habit_name
        self.template_id = template_id
        self.category_id = category_id
        self.description = description
        self.goal = goal
        self.frequency = frequency
        self.created_at = created_at
    

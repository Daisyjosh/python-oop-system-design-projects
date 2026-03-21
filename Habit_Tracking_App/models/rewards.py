class Reward:
    def __init__(self, reward_id, title, criteria_type, criteria_value, reward_type, description, created_at=None):
        self.reward_id = reward_id
        self.reward_title = title
        self.criteria_type = criteria_type
        self.criteria_value = criteria_value 
        self.reward_type = reward_type
        self.description = description
        self.created_at = created_at

    def __str__(self):
        return f"{self.reward_title} ({self.criteria_type} - {self.criteria_value})"
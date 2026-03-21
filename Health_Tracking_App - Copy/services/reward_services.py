from models.rewards import Reward

class RewardService:
    def __init__(self,db):
        self.db = db

    def get_user_rewards(self,user_id):
        query = """SELECT r.reward_title FROM user_rewards ur JOIN rewards r ON ur.reward_id = r.reward_id WHERE ur.user_id = ?"""
        return self.db.fetch_all(query,(user_id,))
    
    def get_available_rewards(self,user_id):
        query = """SELECT * FROM rewards WHERE reward_id NOT IN (SELECT reward_id FROM user_rewards WHERE user_id = ?)"""
        rows = self.db.fetch_all(query,(user_id,))
        return [Reward(*row) for row in rows]
    
    def get_all_rewards(self):
        query = "SELECT * FROM rewards"

        rows = self.db.fetch_all(query)

        rewards = []
        for row in rows:
            rewards.append(Reward(reward_id=row[0],title=row[1],
            criteria_type=row[2],
            criteria_value=row[3],
            reward_type=row[4],
            description=row[5],
            created_at=row[6]))
        return rewards
    

    def assign_rewards(self,user_id,reward_id):
        query = """INSERT INTO user_rewards(user_id,reward_id) VALUES(?,?)"""
        self.db.execute(query,(user_id,reward_id))

    
    def has_reward(self,user_id,reward_id):
        query = """SELECT 1 FROM user_rewards WHERE user_id = ? AND reward_id = ?"""

        return self.db.fetch_one(query,(user_id,reward_id)) is not None
    

    def check_and_assign_rewards(self,user_id,habit_id,habit_service):
        rewards = self.get_all_rewards()

        for reward in rewards:
            if self.had_reward(user_id,reward.reward_id):
                continue

            if reward.criteria_type =='streak':
                streak = habit_service.calculate_streak(habit_id)
                if streak >= reward.criteria_value:
                    self.assign_rewards(user_id,reward.reward_id)
                    print(f"🏆 Reward Unlocked: {reward.title}")

                elif reward.criteia_type == 'points':
                    user = self.db.fetch_one("SELECT points FROM users WHERE user_id = ?",(user_id,))
                    if user[0] >= reward.criteria_value:
                        self.assign_rewards(user_id,reward.reward_id)
                        print(f"🏆 Reward Unlocked: {reward.title}")

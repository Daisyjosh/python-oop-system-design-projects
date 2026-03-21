from models.habit_category import HabitCategory
from models.habit_template import HabitTemplate
from models.habit import Habit
from services.reward_services import RewardService
from datetime import datetime, timedelta,date

class HabitService:
    POINTS_PER_COMPLETION = 10
    def __init__(self, db):
        self.db = db
        self.reward_service = RewardService(self.db)
    def create_habit(self, habit):
        query = """
        INSERT INTO habit(user_id, habit_name, template_id, category_id, description, goal, frequency)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        
        self.db.cursor.execute(query, (
            habit.user_id,
            habit.habit_name,
            habit.template_id,
            habit.category_id,
            habit.description,
            habit.goal,
            habit.frequency
        ))
    
        self.db.conn.commit()

        habit.habit_id = self.db.cursor.lastrowid

    def get_user_habits(self, user_id):
        query = """SELECT habit_id, user_id, habit_name, template_id, category_id, description,goal,frequency,created_at FROM habit WHERE user_id = ?"""

        rows = self.db.fetch_all(query,(user_id,))

        habits = []
        for row in rows:
            habits.append(Habit(
            user_id=row[1],
            habit_name=row[2],
            template_id=row[3],
            category_id=row[4],
            description=row[5],
            goal=row[6],
            frequency=row[7],
            habit_id=row[0],
            created_at=row[8]
        ))
        return habits


    def get_categories(self):
        query = "SELECT * FROM habit_category"
        rows = self.db.fetch_all(query,())

        categories = []
        for row in rows:
            categories.append(HabitCategory(*row))
        return categories

    def get_templates(self):
        query = "SELECT * FROM habit_template"
        rows = self.db.fetch_all(query,())

        templates = []
        for row in rows:
            templates.append(HabitTemplate(*row))
        return templates
    
    def log_habit(self, habit_id, user_id, status,reward_service):
        query_check = """SELECT 1 FROM habit WHERE habit_id = ? AND user_id = ?"""
        result = self.db.fetch_one(query_check,(habit_id,user_id))

        if not result:
            raise ValueError("Invalid Habit ID")

        query = """INSERT INTO habit_log(habit_id,log_date,status) VALUES(?,DATE('now'),?)"""
        self.db.execute(query,(habit_id,status))

        points = 0

        if status == 1:
            points += self.POINTS_PER_COMPLETION

            streak = self.calculate_streak(habit_id)
            weekly = self.get_weekly_completion(habit_id)

            points += self.get_streak_bonus(user_id,habit_id,streak)
            points += self.get_weekly_bonus(user_id,habit_id,weekly)

            self.update_user_points(user_id,points)

        reward_service.check_and_assign_rewards(user_id,habit_id,self)
        return points

    
    
    def update_user_points(self,user_id,points_to_add):
        query = """UPDATE users SET points = points + ? WHERE user_id = ?"""
        self.db.execute(query,(points_to_add,user_id))

    def calculate_streak(self,habit_id):
        query = """SELECT log_date FROM habit_log WHERE habit_id = ? AND status = 1 ORDER BY log_date DESC"""
        
        rows = self.db.fetch_all(query,(habit_id,))

        streak = 0
        today = datetime.today().date()

        for i,row in enumerate(rows):
            expected_date = today - timedelta(days=i)
            log_date = datetime.strptime(row[0],"%Y-%m-%d").date()

            if log_date == expected_date:
                streak+=1
            else:
                break
        return streak
    def get_weekly_completion(self,habit_id):
        query = """SELECT COUNT(*) FROM habit_log WHERE habit_id = ? AND status = 1 AND log_date >= DATE('now','-7 days')"""

        result = self.db.fetch_one(query,(habit_id,))
        return result[0]
    
    def get_streak_bonus(self, user_id, habit_id, streak):
        if streak not in (3, 7):
            return 0

        today = date.today()

        query = """
        SELECT 1 FROM user_bonus 
        WHERE user_id = ? AND habit_id = ? 
        AND bonus_type = 'streak' AND bonus_date = ?
        """

        exists = self.db.fetch_one(query,(user_id,habit_id,today))

        if exists:
            return 0

        insert_query = """
        INSERT INTO user_bonus(user_id,habit_id,bonus_type,bonus_date)
        VALUES(?,?,'streak',?)
        """

        self.db.execute(insert_query,(user_id,habit_id,today))

        if streak == 3:
            return 50
        elif streak == 7:
            return 100
        
    
    def get_weekly_bonus(self,user_id,habit_id,weekly_count):
        if weekly_count < 5:
            return 0

        query = """
        SELECT 1 FROM user_bonus 
        WHERE user_id = ? AND habit_id = ? 
        AND bonus_type = 'weekly' 
        AND bonus_date >= DATE('now', '-7 days')
        """

        exists = self.db.fetch_one(query,(user_id,habit_id))

        if exists:
            return 0

        insert_query = """
        INSERT INTO user_bonus(user_id,habit_id,bonus_type,bonus_date)
        VALUES(?,?,'weekly',DATE('now'))
        """

        self.db.execute(insert_query,(user_id,habit_id))

        return 100
    
    def get_longest_streak(self,habit_id):
        query = """SELECT log_date FROM habit_log WHERE habit_id = ? AND status = 1 ORDER BY log_date"""

        rows = self.db.fetch_all(query,(habit_id,))

        if not rows:
            return 0
        
        longest = 0
        current = 0
        prev_date = None

        for row in rows:
            log_date = datetime.strptime(row[0], "%Y-%m-%d").date()

            if prev_date is None:
                current = 1
            else:
                if log_date == prev_date + timedelta(days=1):
                    current+=1
                else:
                    current=1
            longest =max(longest,current)
            prev_date = log_date
        return longest
    
    


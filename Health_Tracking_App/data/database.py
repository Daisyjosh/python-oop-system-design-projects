import sqlite3

class DatabaseHandlder():
    def __init__(self):
        self.conn = sqlite3.connect("habit_tracker.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.create_tables()
        self.seed_data()

    def create_tables(self):

        # USERS
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            email_id TEXT UNIQUE,
            phone_no TEXT UNIQUE,
            password_hash TEXT NOT NULL,
            reminder_time TEXT,
            points INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)


        # HABIT TEMPLATE
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS habit_template (
            template_id INTEGER PRIMARY KEY AUTOINCREMENT,
            template_name TEXT NOT NULL UNIQUE
        );
        """)


        # HABIT CATEGORY
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS habit_category (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL UNIQUE
        );
        """)


        # HABIT
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS habit (
            habit_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            habit_name TEXT NOT NULL,
            template_id INTEGER,
            category_id INTEGER NOT NULL,
            description TEXT,
            goal TEXT NOT NULL,
            frequency TEXT CHECK(frequency IN ('Daily','Weekly','Monthly')),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (template_id) REFERENCES habit_template(template_id),
            FOREIGN KEY (category_id) REFERENCES habit_category(category_id)
        );
        """)


        # REWARDS
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS rewards (
            reward_id INTEGER PRIMARY KEY AUTOINCREMENT,
            reward_title TEXT NOT NULL,
            criteria_type TEXT CHECK(criteria_type IN ('streak','points','level')),
            criteria_value INTEGER NOT NULL,
            reward_type TEXT CHECK(reward_type IN ('badge','level','milestone')),
            description TEXT,
            created_at DATETIME DEFAULT CURRENT_DATETIME,
            UNIQUE(reward_title,criteria_type,criteria_value)
        );
        """)


        # USER REWARDS
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_rewards (
            user_reward_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            reward_id INTEGER NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id,reward_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (reward_id) REFERENCES rewards(reward_id)
        );
        """)


        # HABIT LOG
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS habit_log (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER NOT NULL,
            log_date DATE NOT NULL,
            status INTEGER DEFAULT 0,

            UNIQUE(habit_id, log_date),

            FOREIGN KEY (habit_id) REFERENCES habit(habit_id)
        );
        """)


        # REMINDER
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminder (
            reminder_id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER NOT NULL,
            reminder_time TEXT,
            frequency TEXT CHECK(frequency IN ('Daily','Weekly','Monthly')),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (habit_id) REFERENCES habit(habit_id)
        );
        """)


        # NOTIFICATION
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS notification (
            notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            type TEXT CHECK(type IN ('reward','connection_request','connection_accept')),
            message TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
        """)


        # JOURNAL
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS journal (
            journal_id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER NOT NULL,
            content TEXT,
            mood TEXT CHECK(mood IN ('Active','Lazy','Motivated','Feeling Low','Dizzy')),
            challenges_faced TEXT,
            obstacles TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (habit_id) REFERENCES habit(habit_id)
        );
        """)


        # CONNECTION
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS connection (
            connection_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            friend_id INTEGER NOT NULL,
            status TEXT CHECK(status IN ('Pending','Accepted','Rejected','Blocked')),
            connected_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (friend_id) REFERENCES users(user_id)
        );
        """)


        # COMMUNITY
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS community (
            community_id INTEGER PRIMARY KEY AUTOINCREMENT,
            community_name TEXT NOT NULL,
            description TEXT,
            created_by INTEGER NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (created_by) REFERENCES users(user_id)
        );
        """)


        # COMMUNITY MEMBER
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS community_member (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            community_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            status TEXT CHECK(status IN ('Pending','Member','Rejected')),
            joined_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (community_id) REFERENCES community(community_id)
        );
        """)


        # POST
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS post (
            post_id INTEGER PRIMARY KEY AUTOINCREMENT,
            community_id INTEGER,
            user_id INTEGER NOT NULL,
            content TEXT,
            type TEXT CHECK(type IN ('journal','badge','level_completion','milestone_achievement')),
            reward_id INTEGER,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (community_id) REFERENCES community(community_id),
            FOREIGN KEY (reward_id) REFERENCES user_rewards(user_reward_id)
        );
        """)


        # COMMENT
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS comment (
            comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            post_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (post_id) REFERENCES post(post_id)
        );

                            
        """)
        # --- bonus_log ---
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_bonus(
            bonus_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            habit_id INTEGER NOT NULL,
            bonus_type TEXT CHECK(bonus_type in ('streak','weekly')),
            bonus_date DATE NOT NULL,

            UNIQUE(user_id,habit_id,bonus_date,bonus_type),

            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (habit_id) REFERENCES habit(habit_id)
        );
        """)
        self.conn.commit()

    

    def seed_rewards(self):
        rewards = [('3 Day Starter 🔥', 'streak', 3, 'badge', 'Great start!'),
        ('7 Day Warrior ⚔️', 'streak', 7, 'badge', 'One week strong!'),
        ('30 Day Champion 🏆', 'streak', 30, 'milestone', '1 month consistency!'),
        ('100 Day Legend 👑', 'streak', 100, 'milestone', 'Legendary streak!'),('100 Points Club ⭐', 'points', 100, 'badge', 'First milestone'),
        ('500 Points Pro 🚀', 'points', 500, 'milestone', 'Pro level'),
        ('1000 Points Master 💎', 'points', 1000, 'milestone', 'Master level'),('Level 1 User 🥉', 'level', 10, 'level', 'Getting started'),
        ('Level 2 User 🥈', 'level', 50, 'level', 'Improving'),
        ('Level 3 User 🥇', 'level', 100, 'level', 'Consistent'),('10 Habits Done 🎯', 'habit_count', 10, 'badge', 'Nice start'),
        ('50 Habits Done 🔥', 'habit_count', 50, 'milestone', 'Strong effort'),]

        for reward in rewards:
            self.cursor.execute("""INSERT OR IGNORE INTO rewards (reward_title, criteria_type, criteria_value, reward_type, description) VALUES(?,?,?,?,?)""",reward)
        self.conn.commit()
    def seed_data(self):
        # ----- CATEGORIES TABLE ------
        categories = ['Health','Fitness','Productivity','Study','Reduce Screen Time','Interact With Parents','LifeStyle']
        for category in categories:
            self.cursor.execute("INSERT OR IGNORE INTO habit_category(category_name) VALUES(?)",(category,))

        # ----- TEMPLATES TABLE -------
        templates = ["Drink 8 glasses of Water","30 minutes excercise","Read 10 pages",'Meditate for 10 minutes','Sleep 7 hours','Write Journal','Interact with parent for 10 minutes','Interact with friends for 10 minutes','Eat one fruit every day']
        for template in templates:
            self.cursor.execute("INSERT OR IGNORE INTO habit_template(template_name) VALUES(?)",(template,))

        # ----- REWARD TABLE ------
        self.seed_rewards()

        
        self.conn.commit()
    def execute(self,query,values=()):
        self.cursor.execute(query,values)
        self.conn.commit()
    def fetch_one(self,query,value=()):
        self.cursor.execute(query,value)
        return self.cursor.fetchone()
    def fetch_all(self,query,value=()):
        self.cursor.execute(query,value)
        return self.cursor.fetchall()
    def close(self):
        self.conn.close()

        
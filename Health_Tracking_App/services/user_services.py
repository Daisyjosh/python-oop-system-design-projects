from models.user import User
class UserService:
    def __init__(self,db):
        self.db = db

    def register(self, user_name, email, phone, password, reminder_time):
        query = """
        INSERT INTO users(user_name, email_id, phone_no, password_hash, reminder_time)
        VALUES (?, ?, ?, ?, ?)
        """
        self.db.execute(query, (user_name,email,phone,password,reminder_time))

    def login(self, email, password):
        query = "SELECT * FROM users WHERE email_id=? AND password_hash=?"
        user_data = self.db.fetch_one(query, (email, password))
        
        if user_data:
            return User(*user_data)
        return None
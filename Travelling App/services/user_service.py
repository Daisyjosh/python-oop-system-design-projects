from models.user import User
class UserService:
    def __init__(self, db):
        self.db = db

    def create_user(self, user):
        self.db.cursor.execute(
            "INSERT INTO users (name,email,password) VALUES (?, ?, ?)",
            (user.name, user.email,user.password)
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid
    
    def get_user_by_email(self, email):
        self.db.cursor.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )
        data = self.db.cursor.fetchone()

        if data:
            return User(data[0], data[1], data[2],data[3])
        return None
        
    def login_user(self, email, password):
        self.db.cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )
        data = self.db.cursor.fetchone()

        if data:
            return User(data[0], data[1], data[2], data[3])  
        return None
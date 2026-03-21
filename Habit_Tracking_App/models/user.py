from data.database import DatabaseHandlder

class User:
    def __init__(self,user_id,name,email,phone,password,reminder_time,points,created_at = None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.reminder_time = reminder_time
        self.points = points
        self.created_at = created_at

    def __str__(self):
        return f"User({self.user_id}, {self.name})"
class NotificationService:
    def __init__(self, db):
        self.db = db

    def create_notification(self, user_id, type, message):
            query = """
            INSERT INTO notification(user_id, type, message)
            VALUES (?, ?, ?)
            """
            self.db.execute(query, (user_id, type, message))

    def get_notifications(self, user_id):
        query = """
        SELECT message, created_at
        FROM notification
        WHERE user_id = ?
        ORDER BY created_at DESC
        """
        return self.db.fetch_all(query, (user_id,))
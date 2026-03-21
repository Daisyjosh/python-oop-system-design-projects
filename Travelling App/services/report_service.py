from datetime import datetime, timedelta

class ReportService:
    def __init__(self, db):
        self.db = db

    def upcoming_items(self, user_id):
        today = datetime.now()
        next_30 = today + timedelta(days=30)

        query = """
        SELECT it.title, i.name, i.date
        FROM itineraries it
        JOIN items i ON it.itinerary_id = i.itinerary_id
        WHERE it.user_id = ?
        AND date(i.date) BETWEEN date(?) AND date(?)
        """

        self.db.cursor.execute(query, (
            user_id,
            today.strftime("%Y-%m-%d"),
            next_30.strftime("%Y-%m-%d")
        ))

        return self.db.cursor.fetchall()

class ItineraryService:
    def __init__(self, db):
        self.db = db

    def create_itinerary(self, itinerary):
        self.db.cursor.execute(
            "INSERT INTO itineraries (user_id, title) VALUES (?, ?)",
            (itinerary.user_id, itinerary.title)
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def add_item(self, item):
        self.db.cursor.execute("""
        INSERT INTO items (itinerary_id, name, description, date, time, cost)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (item.itinerary_id, item.name, item.description, item.date, item.time, item.cost))
        self.db.conn.commit()

    def get_all_itineraries(self, user_id):
        self.db.cursor.execute(
            "SELECT * FROM itineraries WHERE user_id=?",
            (user_id,)
        )
        return self.db.cursor.fetchall()


    def get_user_itineraries(self, user_id):
        self.db.cursor.execute(
            "SELECT * FROM itineraries WHERE user_id=?",
            (user_id,)
        )
        return self.db.cursor.fetchall()


    def delete_itinerary(self, itinerary_id):
        self.db.cursor.execute(
            "DELETE FROM items WHERE itinerary_id=?",
            (itinerary_id,)
        )

        self.db.cursor.execute(
            "DELETE FROM itineraries WHERE itinerary_id=?",
            (itinerary_id,)
        )

        self.db.conn.commit()
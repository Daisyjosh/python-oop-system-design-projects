class BookingService:
    def __init__(self, db):
        self.db = db

    def create_booking(self, booking):
        self.db.cursor.execute("""
        INSERT INTO bookings (user_id, type, details, date, cost)
        VALUES (?, ?, ?, ?, ?)
        """, (booking.user_id, booking.type, booking.details, booking.date, booking.cost))
        self.db.conn.commit()
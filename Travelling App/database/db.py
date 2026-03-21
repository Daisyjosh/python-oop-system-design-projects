import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("travel_app.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS itineraries (
            itinerary_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            itinerary_id INTEGER,
            name TEXT,
            description TEXT,
            date TEXT,
            time TEXT,
            FOREIGN KEY(itinerary_id) REFERENCES itineraries(itinerary_id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,  -- hotel / transport
            details TEXT,
            date TEXT,
            cost REAL,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            amount REAL,
            date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            destination TEXT,
            rating INTEGER,
            comment TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
        """)

        self.conn.commit()
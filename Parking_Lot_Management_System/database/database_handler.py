import sqlite3

class DatabaseHandler:

    def __init__(self):
        self.connection = sqlite3.connect("parking_lot.db")
        self.cursor = self.connection.cursor()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS parking_slot(
            slot_id INTEGER PRIMARY KEY,
            slot_type TEXT,
            status TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicle(
            vehicle_number TEXT PRIMARY KEY,
            vehicle_type TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS ticket(
            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_number TEXT,
            slot_id INTEGER,
            entry_time TEXT,
            exit_time TEXT
        )
        """)

        self.connection.commit()

    def add_vehicle(self, vehicle_number, vehicle_type):

        self.cursor.execute("""
        INSERT OR IGNORE INTO vehicle VALUES (?,?)
        """,(vehicle_number,vehicle_type))

        self.connection.commit()

    def create_ticket(self, vehicle_number, slot_id, entry_time):

        self.cursor.execute("""
        INSERT INTO ticket(vehicle_number,slot_id,entry_time)
        VALUES (?,?,?)
        """,(vehicle_number,slot_id,entry_time))

        self.connection.commit()

        return self.cursor.lastrowid

    def close_ticket(self, ticket_id, exit_time):

        self.cursor.execute("""
        UPDATE ticket
        SET exit_time=?
        WHERE ticket_id=?
        """,(exit_time,ticket_id))

        self.connection.commit()

    def update_slot_status(self, slot_id, status):

        self.cursor.execute("""
        UPDATE parking_slot
        SET status=?
        WHERE slot_id=?
        """,(status,slot_id))

        self.connection.commit()

    def add_slot(self, slot_id, slot_type):

        self.cursor.execute("""
        INSERT OR IGNORE INTO parking_slot VALUES (?,?,?)
        """,(slot_id,slot_type,"FREE"))

        self.connection.commit()

    def get_free_slot(self):

        self.cursor.execute("""
        SELECT slot_id FROM parking_slot
        WHERE status='FREE'
        LIMIT 1
        """)

        return self.cursor.fetchone()

    def close(self):
        self.connection.close()
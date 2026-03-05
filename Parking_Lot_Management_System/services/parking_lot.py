from database.database_handler import DatabaseHandler
import datetime

class ParkingLot:

    def __init__(self):
        self.db = DatabaseHandler()
        self.db.create_tables()

    def add_slot(self, slot_id, slot_type):
        self.db.add_slot(slot_id,slot_type)

    def park_vehicle(self, vehicle_number, vehicle_type):

        free_slot = self.db.get_free_slot()

        if not free_slot:
            print("No slot available")
            return

        slot_id = free_slot[0]

        entry_time = datetime.datetime.now()

        self.db.add_vehicle(vehicle_number,vehicle_type)

        ticket_id = self.db.create_ticket(
            vehicle_number,
            slot_id,
            entry_time
        )

        self.db.update_slot_status(slot_id,"OCCUPIED")

        print("Vehicle parked")
        print("Ticket ID:",ticket_id)
        print("Slot:",slot_id)

    def exit_vehicle(self,ticket_id):

        exit_time = datetime.datetime.now()

        self.db.close_ticket(ticket_id,exit_time)

        print("Vehicle exited")
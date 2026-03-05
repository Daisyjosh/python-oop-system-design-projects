class Ticket:

    def __init__(self, ticket_id, vehicle_number, slot_id, entry_time):
        self.ticket_id = ticket_id
        self.vehicle_number = vehicle_number
        self.slot_id = slot_id
        self.entry_time = entry_time
        self.exit_time = None

    def close_ticket(self, exit_time):
        self.exit_time = exit_time
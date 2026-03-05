class Floor:

    def __init__(self,floor_id):
        self.floor_id = floor_id
        self.slots = []

    def add_slot(self,slot):
        self.slots.append(slot)
    

    def get_available_slot(self):
        for slot in self.slots:
            if not slot.is_occupied:
                return slot
        return None
    
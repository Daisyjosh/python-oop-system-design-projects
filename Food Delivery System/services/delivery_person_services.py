class DeliveryPersonServices:
    def __init__(self):
        self.delivery_partners = {}
    
    def add_delivery_person(self,dp):
        self.delivery_partners[dp.id] = dp

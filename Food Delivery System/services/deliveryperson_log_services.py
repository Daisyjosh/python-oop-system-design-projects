class DeliveryPersonLogServices:
    def __init__(self):
        self.logs = {}

    def add_logs(self,l):
        self.logs[l.log_id] = l
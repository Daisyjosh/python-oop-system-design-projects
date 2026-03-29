class FarmerController:
    def __init__(self,farmer_services):
        self.farmer_service = farmer_services

    def add_product(self,product_name,farmer_id,base_price,description,created_at):
        
        self.farmer_service.add_product(product_name,farmer_id,base_price,description,created_at)


        
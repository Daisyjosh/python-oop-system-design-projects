class FarmerService:
    def __init__(self,farmer_repo,product_services):
        self.farmer_repo = farmer_repo
        self.product_services = product_services

    def add_product(self,product_name,farmer_id,base_price,description,created_at):
        self.product_services.add_product(product_name,farmer_id,base_price,description,created_at)
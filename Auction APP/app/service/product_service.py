from app.model.product import Product
from datetime import date
class ProductService:
    def __init__(self,product_repo):
        self.product_repo = product_repo
        
    def add_product(self,product_name,farmer_id,base_price,description,created_at):
        product_no = len(self.product_repo.products)+1
        product_id = "P" + str(product_no)
        p = Product(product_id,product_name,farmer_id,base_price,description,date.today())
        self.product_repo.add(p)

    
        

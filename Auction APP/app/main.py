from app.repository.farmer_repository import FarmerRepository
from app.repository.retailer_repository import RetailerRepository
from app.repository.product_repository import ProductRepository
from app.model.product import Product
from app.controller.farmer_controller import FarmerController
from app.controller.retailer_controller import RetailerController
from app.service.farmer_service import FarmerService
from app.service.retailer_service import RetailerService
from app.service.product_service import ProductService
from app.view.app_view import AppView
from 


def main():
    farmer_repo = FarmerRepository()
    retailer_repo = RetailerRepository()
    product_repo = ProductRepository()
    product_service = ProductService(product_repo)
    farmer_service = FarmerService(farmer_repo,product_service)
    retailer_service = RetailerService(retailer_repo)
    farmer_controller = FarmerController(farmer_service)
    retailer_controller = RetailerController(retailer_service)
    view = AppView(farmer_controller,retailer_controller)
    view.start()

if __name__ == "__main__":
    main()


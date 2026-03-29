class CustomerController:
    def __init__(self,customer_service,usercart_service,menu_service,review_service,order_service):
        self.customer_service = customer_service
        self.usercart_service = usercart_service
        self.menu_service = menu_service
        self.review_services = review_service
        self.order_service = order_service

    def add_cart(self,customer_id,cart_items,created_at):
        return self.usercart_service.add_cart(customer_id,cart_items,created_at)
    
    def show_menu(self):
        self.menu_service.show_menu()

    def view_cust_cart(self,cart_id):
        self.usercart_service.view_cust_cart(cart_id)

    def write_review(self,cust_id,order_id,rev_type,rating,comment,created_at):
        self.review_services.add_cust_review(cust_id,order_id,rev_type,rating,comment,created_at)
  
    def place_order(self,cust_id,cart_id,dp_id,status,created_at):
        return self.order_service.place_order(cust_id,cart_id,dp_id,status,created_at)
    

    def view_reviews(self,cust_id):
        self.review_services.get_reviews(cust_id)

    def get_menu(self,menu_id):
        return self.menu_service.get(menu_id)
    
    def view_history(self,cust_id):
        self.order_service.get_orders(cust_id)
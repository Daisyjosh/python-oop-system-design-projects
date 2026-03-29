from app.model.user_cart import UserCart
class UserCartService:
    def __init__(self,usercart_repo):
        self.usercart_repo = usercart_repo

    def add_cart(self,cust_id,cart_items,created_at):
        cart_no = len(self.usercart_repo.cart)+1
        cart_id = "CART"+str(cart_no)
        cart = UserCart(cart_id,cust_id,cart_items,created_at)
        self.usercart_repo.add(cart)
        return cart.cart_id

    def view_cust_cart(self,cart_id):
        self.usercart_repo.customer_cart(cart_id)

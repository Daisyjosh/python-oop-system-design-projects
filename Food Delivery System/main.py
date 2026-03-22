from models.user import User
from models.customer import Customer
from models.restaurant import Restaurant
from models.delivery_person import DeliveryPerson
from models.order import Order
from models.menu import Menu
from models.user_cart import UserCart
from models.customer_review import CustomerReview
from models.delivery_person_review import DeliveryPersonReview
from services.customer_services import CustomerService
from services.users_services import UserServices
from services.restaurant_services import RestaurantServices
from services.delivery_person_services import DeliveryPersonServices
from services.menu_services import MenuServices
from services.usercart_services import UserCartServices
from services.order_services import OrderServices
from services.reviews_services import ReviewServices
class FoodiesStop:
    def __init__(self):
        self.customer_services = CustomerService()
        self.user_services = UserServices()
        self.restaurant_services = RestaurantServices()
        self.delivery_person_services = DeliveryPersonServices()
        self.menu_services = MenuServices()
        self.usercart_services = UserCartServices()
        self.order_services = OrderServices()
        self.review_services = ReviewServices()
    
    def load_data_customer(self):
        c1 = Customer(1,"Daisy","daisypotes93@gmail.com","7894561234","Coimbatore")
        c2 = Customer(2,"Alice Mary","alice2005@gmail.com","4567891235","Tuticorin")
        self.customer_services.add_customer(c1)
        self.customer_services.add_customer(c2)
        self.user_services.add_users(c1)
        self.user_services.add_users(c2)

    def load_data_restaurant(self):
        r1 = Restaurant(1,"Alice Hotel","Tuticorin","7am","10pm")
        r2 = Restaurant(2,"Rebecca Hotel","Dharmapuri","7am","11pm")
        self.restaurant_services.add_restaurant(r1)
        self.restaurant_services.add_restaurant(r2)
        self.user_services.add_users(r1)
        self.user_services.add_users(r2)

    def load_data_deliverPerson(self):
        dp1 = DeliveryPerson(1,"DaisyRider","drider@gmail.com","5555555555","Coimbatore","6226")
        dp2 = DeliveryPerson(2,"JoshuaRider","jrider@gmail.com","7894565454","Coimbatore","7447")
        self.delivery_person_services.add_delivery_person(dp1)
        self.delivery_person_services.add_delivery_person(dp2)

    def load_data_menu(self):
        m1 = Menu(1,1,"Dosa",100)
        m2 = Menu(2,1,"Poori",90)
        m3 = Menu(3,1,"Veg Biriyani",200)
        m4 = Menu(4,2,"Non Veg Meals","250")
        m5 = Menu(5,2,"Veg Meals",150)
        m6 = Menu(6,2,"Chicken Biriyani",200)
        self.menu_services.add_menu(m1)
        self.menu_services.add_menu(m2)
        self.menu_services.add_menu(m3)
        self.menu_services.add_menu(m4)
        self.menu_services.add_menu(m5)
        self.menu_services.add_menu(m6)
    

    def load_cart_data(self):
        ct1 = UserCart(1,1,1)
        ct2 = UserCart(2,2,1)
        self.usercart_services.add_to_cart(ct1)
        self.usercart_services.add_to_cart(ct2)
    
    def load_order(self):
        o = Order(1,1,1)
        self.order_services.add_order(o)
    
    def write_review_customer(self):
        Creview1 = CustomerReview(1,1,"Restaurant","Good Food",4.5)
        Creview2 = CustomerReview(2,1,"DeliveryPerson","Fast Delivery",5)
        self.review_services.add_reviews(Creview1)
        self.review_services.add_reviews(Creview2)

    def write_review_delivery_person(self):
        DPreview1 = DeliveryPersonReview(1,1,"Restaurant","Well Packed, Friendly Employees",5)
        self.review_services.add_reviews(DPreview1)
        
        






    




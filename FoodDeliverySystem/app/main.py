from app.view.app_view import CustomerView
from app.model.menu import Menu
from app.model.customer import Customer
from app.model.deliveryperson import DeliveryPerson
from app.model.restaurant import Restaurant
from datetime import date
from app.service.order_service import OrderService
from app.service.customer_service import CustomerService
from app.service.menu_service import MenuService
from app.service.restaurant_service import RestaurantService
from app.service.usercart_service import UserCartService
from app.service.review_service import ReviewService
from app.repository.customer_repo import CustomerRepo
from app.repository.restaurant_repo import RestaurantRepo
from app.repository.usercart_repo import UserCartRepo
from app.repository.menu_repo import MenuRepo
from app.repository.review_repo import ReviewRepo
from app.repository.order_repo import OrderRepo
from app.controller.customer_controller import CustomerController



def main():
    menu_repo = MenuRepo()
    menu_service = MenuService(menu_repo)
    cart_repo = UserCartRepo(menu_service)
    usercart_services = UserCartService(cart_repo)
    review_repo = ReviewRepo()
    review_service = ReviewService(review_repo)
    order_repo = OrderRepo(cart_repo)
    order_service = OrderService(order_repo)
    customer_repo = CustomerRepo()
    customer_service = CustomerService(customer_repo)
    customer_controller = CustomerController(customer_service,usercart_services,menu_service,review_service,order_service)
    rest_repo = RestaurantRepo()
    restaurant_service = RestaurantService(rest_repo)
    customer_view = CustomerView(customer_controller)

    





    #seed data
    r1 = Restaurant("R1","Alice Hotel","ALice Sagaya Mary","alice@gmail.com",123456,"R",date.today())
    r2 = Restaurant("R2","Joshua's Hotel","Joshua","josh@gmail.com",123464,"T",date.today())
    restaurant_service.add_restaurant(r1)
    restaurant_service.add_restaurant(r2)
    c1 = Customer("C1",1,"Daisy","daisy@gmail.com",123456,"C",date.today())
    customer_service.add_customer(c1)
    dp1 = DeliveryPerson("DP1",2,"Aron","aron@gmail.com",123456,"G",date.today())
    dp2 = DeliveryPerson("Dp2",3,"Rider","rider@gmail.com",123456,"F",date.today())
    m1 = Menu("M1","R1","Dosa","Crispy Dosa",100,date.today())
    m2 = Menu("M2","R1","Idly","Ball like idly",200,date.today())
    m3 = Menu("M3","R1","Idiyappam","Healthy Noodles",400,date.today())
    m4 = Menu("M4","R2","Veg Biriyani","Mixed Veggy Yummy Biriyani",100,date.today())
    m5 = Menu("M5","R2","Chicken Biriyani","Spicy Flavourful Biriyani",200,date.today())
    m6 = Menu("M6","R2","Mutton Biriyani","Spicy Flavourful Biriyani",400,date.today())
    menu_service.add_menu(m1)
    menu_service.add_menu(m2)
    menu_service.add_menu(m3)
    menu_service.add_menu(m4)
    menu_service.add_menu(m5)
    menu_service.add_menu(m6)
    

    customer_view.start()

if __name__ == "__main__":
    main()
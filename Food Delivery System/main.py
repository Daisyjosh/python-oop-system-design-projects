from models.customer import Customer
from models.restaurant import Restaurant
from models.delivery_person import DeliveryPerson
from models.order import Order
from models.menu import Menu
from models.delivery_person_log import DeliveryPersonLog
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
from services.deliveryperson_log_services import DeliveryPersonLogServices
class FoodiesStop:
    def __init__(self):
        self.customer_services = CustomerService()
        self.user_services = UserServices()
        self.restaurant_services = RestaurantServices()
        self.delivery_person_services = DeliveryPersonServices()
        self.usercart_services = UserCartServices()
        self.menu_services = MenuServices(self.usercart_services)
        self.order_services = OrderServices(self.usercart_services)
        self.review_services = ReviewServices(self.order_services)
        self.delivery_person_log_services = DeliveryPersonLogServices()
        self.usercart_services.menu_services = self.menu_services
        self.load_data_menu()
        self.current_user_id = 1
    
    def start_application(self):
        print("========== WELCOME TO FOODIES STOP ==========")

        print("========== USER DASHBOARD ==========")
        print("\n1. Login as Customer")
        print("2. Login as Delivery Person")
        print("3. Login as Restaurant")
        print("4. Exit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid Input")
        
        if choice == 1:
            self.login_customer()
        elif choice == 2:
            self.login_delivery_person()
        elif choice == 3:
            self.login_restaurant()
        elif choice == 4:
            return
        else:
            print("Invalid Input")


    def order_food(self):
        
        self.menu_services.show_menu()

        cart_items = {}
        print("Ready to choose your food!!")

        while True:
            try:
                menu_id = int(input("Enter menu_id: "))
                count = int(input("Enter Count: "))
            except ValueError:
                print("❌ Invalid Input")
                continue

            if menu_id not in self.menu_services.menu:
                print("❌ Invalid Menu ID")
                continue

            if count <= 0:
                print("❌ Count must be greater than 0")
                continue
            

            cart_items[menu_id] = cart_items.get(menu_id,0)+count
            
            response = input("Add another item? (yes/no): ").lower()
            if response == "no":
                break
            elif response != "yes":
                print("❌ Invalid Input")
                break

        cart_id = len(self.usercart_services.cart) + 1
        cart = UserCart(cart_id, cart_items,1)
        self.usercart_services.add_to_cart(cart)

        while True:
            print("==== DONE PICKING FOODS ====")
            print("\n1. View Cart")
            print("2. Confirm Order")


            try:
                choice = int(input("Enter Choice: "))
            except ValueError:
                print("❌ Invalid input")
                continue

            if choice == 1:
                self.usercart_services.view_cart(cart.cart_id)
            elif choice == 2:
                cart_id = self.usercart_services.find_cart_id(self.current_user_id)
                if not cart_id:
                    print("❌ No cart found")
                    return
                
                order_id = len(self.order_services.order)+1
                order = Order(order_id,cart_id,self.current_user_id)
                self.order_services.add_order(order)
                print("✅ Order Confirmed!")
                self.confirm_order()
                break
            else:
                print("❌ INVALID INPUT")
    def confirm_order(self):
        print()

    def write_review_customer(self,order_id):
        review_id = len(self.review_services.reviews)+1
        print("========== LEAVE A REVIEW TODAY HAVE A BEST EXPERIENCE TOMORROW ==========")
        while True:
            try:
                review_type = input("\n 1. On Restaurant (R) \n 2. On Delivery Person (DP) \nEnter type of Review: ").lower()
                if review_type in ('dp','r'):
                    break

                print("❌ Invalid Input, try again")
            except ValueError:
                print("❌ Invalid Input")
                break
        comment = input("Enter Your Valuable Comment: ")


        while True:
            try:
                rating = float(input("Enter Ratings for (1-5): "))
                if 1 <= rating <= 5:
                    break
                print("❌ Rating must be between 1 and 5")
            except ValueError:
                print("❌ Invalid Input")
        review = CustomerReview(review_id,order_id,review_type,comment,rating)
        self.review_services.add_reviews(review)

        print(f"\n ========== THANKS FOR YOUR VALUABLE FEEDBACK ON {"RESTAURANT" if review_type == 'r' else "DELIVERY PERSON\n"} =======")

    
    def view_order_history(self,cust_id):
        user_orders = self.order_services.get_user_orders(cust_id)
        if not user_orders:
            print("No orders found.")
            return

        for order in user_orders:
            cart = self.usercart_services.cart.get(order.cart_id)
            
            print(f"\n🧾 Order ID: {order.order_id}")
            print(f"Status: {order.status}")

            print("Items:")
            total = 0
            for menu_id, qty in cart.cart_items.items():
                menu = self.menu_services.get_item(menu_id)
                amount = menu.price * qty
                total += amount
                print(f" -{menu.item_name} (x{qty}) | ₹{amount}")
            print(f"Total Bill Paid: {total}")

    

        


        

                
    def login_customer(self):
        while True:
            print("========== CUSTOMER DASHBOARD ==========")
            print("\n1. Order Food")
            print("2. Write a Review")
            print("3. View History")
            print("4. View Reviews")
            print("5. Logout")   

            choice = int(input("Enter Choice: "))

            if choice == 1:
                print("Order Food")
                self.order_food()
            elif choice == 2:
                cart_id = self.usercart_services.find_cart_id(self.current_user_id)
                if not cart_id:
                    print("❌ No cart found")
                    continue
                order_id = self.order_services.find_order_id(cart_id)
                if not order_id:
                    print("❌ No order found to review")
                    return
                self.write_review_customer(order_id)
            elif choice == 3:
                print("========== VIEW YOUR ORDER HISTORY ==========")
                self.view_order_history(self.current_user_id)
            elif choice == 4:
                print("========== VIEW YOUR PREVIOUS REVIEWS ==========")
                self.review_services.view_reviews(self.current_user_id)
            elif choice == 5:
                print("Logging out...")
                break
            else:
                print("Invalid choice")

    def login_restaurant(self):
        print("=========== RESTAURANT DASHBOARD ==========")
        print("\n 1. View Menu")
        print("2. Add Menu")
        print("3. Delete Menu")
        print("4. View Orders")
        print("5. View Completed Orders")
        print("6. View Reviews")
        print("6. Logout")


    def login_delivery_person(self):
        print("========== DELIVERY PERSON DASHBOARD =========")
        print("\n 1. View Orders")
        print("2. View Completed Orders")
        print("3. Complete an Order")
        print("3. Write Review")
        print("4. View Reviews")
        print("5. Logout")

    




    

    
    
    
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

    def load_data_deliverPerson(self):
        dp1 = DeliveryPerson(1,"DaisyRider","drider@gmail.com","5555555555","Coimbatore","6226")
        dp2 = DeliveryPerson(2,"JoshuaRider","jrider@gmail.com","7894565454","Coimbatore","7447")
        self.delivery_person_services.add_delivery_person(dp1)
        self.delivery_person_services.add_delivery_person(dp2)
        self.user_services.add_users(dp1)
        self.user_services.add_users(dp2)

    def load_data_menu(self):
        m1 = Menu(1,1,"Dosa",100)
        m2 = Menu(2,1,"Poori",90)
        m3 = Menu(3,1,"Veg Biriyani",200)
        m4 = Menu(4,2,"Non Veg Meals",250)
        m5 = Menu(5,2,"Veg Meals",150)
        m6 = Menu(6,2,"Chicken Biriyani",200)
        self.menu_services.add_menu(m1)
        self.menu_services.add_menu(m2)
        self.menu_services.add_menu(m3)
        self.menu_services.add_menu(m4)
        self.menu_services.add_menu(m5)
        self.menu_services.add_menu(m6)
    

    def load_cart_data(self):
        ct1 = UserCart(1,{1:1,2:1},1)
        ct2 = UserCart(2,{2:1,3:1},2)
        self.usercart_services.add_to_cart(ct1)
        self.usercart_services.add_to_cart(ct2)
    
    def load_order(self):
        o = Order(1,1,1)
        self.order_services.add_order(o)
    
    def write_review_customer_data(self):
        Creview1 = CustomerReview(1,1,"Restaurant","Good Food",4.5)
        Creview2 = CustomerReview(2,1,"DeliveryPerson","Fast Delivery",5)
        self.review_services.add_reviews(Creview1)
        self.review_services.add_reviews(Creview2)

    def write_review_delivery_person_data(self):
        DPreview1 = DeliveryPersonReview(1,1,"Restaurant","Well Packed, Friendly Employees",5)
        self.review_services.add_reviews(DPreview1)

    def complete_order_data(self):
        l1 = DeliveryPersonLog(1,1,1,"completed")
        self.delivery_person_log_services.add_logs(l1)
    
    def process_order(self):
        self.load_cart_data()
        self.load_order()
        self.complete_order()
        self.write_review_customer()
        self.write_review_delivery_person()
    

if __name__ == "__main__":
    app = FoodiesStop()
    app.start_application()

        






    




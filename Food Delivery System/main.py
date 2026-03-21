from services.customer_services import CustomerService
from models.delivery_person import DeliveryPerson
from models.user import User
from models.restaurant import Restaurant
class FoodDeliverySystem:
    User(1,"Daisy",1234789652)
    Restaurant(1,"Daisy Hotel",1234567897)
    Restaurant(2,"Joshua Hotel",7894561254)
    Restaurant(3,"Sdhevaan Hotel",4567891235)
    DeliveryPerson(1,"Daisy",1457896528)
    def start_application(self):
        print("====== WELCOME TO FOODIES STOP ======")
        try:
            role = input("Enter Role: ")
        except ValueError:
            print("❌ Invalid Input")
        if role == "Customer":
            self.customer_services()
        elif role == "restaurant":
            self.restaurant_services()
        elif role == "Delivery Person":
            self.DeliveryPerson_services()
        else:
            return
    def customer_services(self):
        print(" ====== CUSTOMER DASHBOARD ========")
        print("1. Order Food")
        print("2. View Orders")
        print("3. Review Order")
        choice = int(input("Enter Choice"))

        if choice == 1:
            self.customer_services.order_food()
        elif choice ==2:
            self.customer_services.View_orders()
        elif choice == 3:
            self.customer_services.review_order()
    

    
    def restaurant_services(self):
        print(" ========= RESTAURANT DASHBOARD =======")
        print("1. View Menu Items")
        print("2. Add Menu Item")
        print("3. Delete Menu Item")
        print("4. Edit Configurations")
        print("5. View Reviews")
        choice = int(input("Enter Choice:"))
        if choice == 1:
            self.restaurant_services.view_menu()
        elif choice == 2:
            self.restaurant_services.Add_Menu()
        elif choice == 3:
            self.restaurant_services.Delete_item()
        elif choice  == 4:
            self.restaurant_services.edit_configuration()
        elif choice == 5:
            self.restaurant_services.view_services()
    
    def DeliveryPerson_services(self):
        print(" ========== Delivery Person Dashboard =========")
        print("1. Check Available Orders")
        print("2. View Reviews")
        print("3. Give Reviews")

        choice = int(input("Enter Choice: "))
        if choice == 1:
            self.
    


        
            
        
        
    

if __name__ == "__main__":
    app = FoodDeliverySystem()
    app.start_application()

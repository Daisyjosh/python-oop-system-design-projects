from datetime import date
class CustomerView:
    def __init__(self,customer_controller):
        self.customer_controller = customer_controller
        self.current_cust_id = "C1"
        self.current_dp_id = "DP1"

    
    def start(self):
        while True:
            print("\n ========== CUSTOMER DASHBOARD ==========")

            self.show_menu()
            try:
                choice = int(input("Enter Choice: "))
            except ValueError:
                print("❌ Invalid Input")

            if choice == 1:
                self.order_food()
            elif choice == 2:
                self.view_reviews()
            elif choice == 3:
                self.view_history()
            elif choice == 4:
                print("Thank You For Visiting Foodies Stop")
                break
            else:
                print("❌ Invalid Input")
    def view_history(self):
        print("========== ORDER HISTORY ==========")
        self.customer_controller.view_history(self.current_cust_id)

    def view_reviews(self):
        print("========== VIEW REVIEWS ===========")
        self.customer_controller.view_reviews(self.current_cust_id)

    
    
    def order_food(self):
        self.show_food_menu()
        print("\n ========== READY TO ORDER THE FOOD =========== \n")
        cart_item = {}
        while True:
            try:
                menu_id = input("Enter Menu ID: ")
                menu = self.customer_controller.get_menu(menu_id)
                
                if not menu:
                    print("❌ Invalid Menu ID")
                    break
            except ValueError:
                print("❌ Invalid Input")
                break
            count = int(input("Enter Count: "))
            if count <= 0:
                print("❌ Invalid COUNT")
                break
            cart_item[menu_id] = cart_item.get(menu_id,0)+count
            try:
                response = input("Wanna Add Extra Food (yes / no): ")
                if response.lower() == "no":
                    break
                elif response.lower() not in ('yes','no'):
                    print("❌ Invalid Input")
                    break

            except ValueError:
                print("❌ Invalid Input")
                return
            

        cart_id = self.customer_controller.add_cart(self.current_cust_id,cart_item,date.today())
        print("\n ========== DONE PICKING FOOD ========== \n")

        while True:
            print("\n1. View Cart")
            print("2. Confirm Order")
        
            try:
                choice = int(input("Enter Choice: "))
            except:
                print("❌ Invalid Input")
                break

            if choice == 1:
                self.view_cart(cart_id)
            elif choice == 2:
                self.confirm_order(cart_id)
                break
            else:
                print("❌ Invalid Input")
        

    def show_food_menu(self):
        self.customer_controller.show_menu()
       
    
    def view_cart(self,cart_id):
        self.customer_controller.view_cust_cart(cart_id)

    def confirm_order(self,cart_id):
        print("✅ Order Confirmed Successfully")
        cart_id = cart_id
        status = "Ordered"
        created_at = date.today()
        order_id = self.customer_controller.place_order(self.current_cust_id,cart_id,self.current_dp_id,status,created_at)
        while True:
            print("\n =========== LEAVE A REVIEW TODAY HAVE A BEST EXPERIENCE TOMORROW ========== \n")
            print("\n1. Write Review on Restaurant: ")
            print("2. Write Review on Delivery Person")
            print("3. No thanks!")
            print("4. Done Reviewing...")
            choice = int(input("Enter Choice: "))
            if choice == 1:
                rev_type = "Restaurant"
                self.write_review(self.current_cust_id,order_id,rev_type)
            elif choice == 2:
                rev_type = "Delivery Person"
                self.write_review(self.current_cust_id,order_id,rev_type)
            elif choice == 3:
                print("Thank You for Order in Foodies Stop!!!")
                break
            elif choice == 4:
                print("Thanks for reviewing on Foodies Stop")
                break
            else:
                print("❌ Invalid Input")
    
    def write_review(self,cust_id,order_id,rev_type):
        try:
            rating = float(input("Enter Rating (1-5): "))
            if rating > 5 or rating <= 0:
                print("❌ Invalid Input")
        except:
            print("❌ Invalid Input")
            return
        
        comment = input("Enter Your Comment: ")
        created_at = date.today()
        self.customer_controller.write_review(cust_id,order_id,rev_type,rating,comment,created_at)
        

    def show_menu(self):
        print("\n1. Order Food")
        print("2. View Reviews")
        print("3. View History")
        print("4. Log Out")
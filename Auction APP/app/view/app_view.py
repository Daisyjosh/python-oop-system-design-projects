from datetime import date
class AppView:
    def __init__(self, farmer_controller, retailer_controller):
        self.farmer_controller = farmer_controller
        self.retailer_controller = retailer_controller

    def start(self):
        while True:
            print("\n1. Farmer Login")
            print("2. Retailer Login")
            print("3. Exit\n")
            try:
                choice = input("Enter choice: ")
            except ValueError:
                print("❌ Invalid Input")
            if choice == "1":
                self.farmer_flow()
            elif choice == "2":
                self.retailer_flow()
            elif choice == "3":
                break
            else:
                print("❌ Invalid Input")

    def farmer_flow(self):
        print("\n ========== Farmer Dashboard ========== \n")
        while True:
            print("1. Add product")
            print("2. Edit Product")
            print("3. View Products")
            print("4. Create Auction")
            print("5. Track Auction")
            print("6. View Reviews")
            print("7. Report Issues")
            print("8. Log Out")

            try:
                choice = int(input("Enter Choice:  "))
            except ValueError:
                print("❌ Invalid Input")
            
            if choice == 1:
                self.add_product()
            elif choice == 2:
                self.edit_product()
            elif choice == 3:
                self.view_product()
            elif choice == 4:
                self.create_auction()
            elif choice == 5:
                self.track_auction()
            elif choice == 6:
                self.view_reviews()
            elif choice == 7:
                self.request_support()
            elif choice == 8:
                return
            else:
                print("❌ Invalid Input")
                
    def add_product(self):
        print("\n ========== ADD PRODUCTS ========== \n")
        product_name = input("Enter Product Name: ")
        farmer_id = input("Enter Farmer ID: ")
        base_price = float(input("Enter Base Price: "))
        description = input("Enter Description: ")
        created_at = date.today()
        print(self.farmer_controller.add_product(product_name,farmer_id,base_price,description,created_at))



    def retailer_flow(self):
        print("Retailer Dashboard")
        # call retailer_controller methods
        # ex: self.retailer_controller.place_bid()
from database.db import Database
from models.user import User
from models.itinerary import Itinerary
from models.item import Item
from models.booking import Booking
from models.expense import Expense

from services.user_service import UserService
from services.itinerary_service import ItineraryService
from services.booking_service import BookingService
from services.expense_service import ExpenseService
from services.report_service import ReportService

from datetime import datetime


class TravelApp:

    def __init__(self):
        self.db = Database()
        self.user_service = UserService(self.db)
        self.itinerary_service = ItineraryService(self.db)
        self.booking_service = BookingService(self.db)
        self.expense_service = ExpenseService(self.db)
        self.report_service = ReportService(self.db)
        self.current_user = None

    def run(self):
        while True:
            print("\n====== TRAVEL PLANNER ======")
            print("1. Register\n2. Login\n3. Exit")

            choice = input("Enter choice: ").strip()

            try:
                if choice == "1":
                    self.register()
                elif choice == "2":
                    self.login()
                elif choice == "3":
                    break
                else:
                    print("Invalid choice")
            except Exception as e:
                print(f"Error: {e}")

    def register(self):
        name = input("Enter name: ").strip()
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()

        if not name or "@" not in email or len(password) < 4:
            print("Invalid input")
            return

        try:
            user_id = self.user_service.create_user(
                User(1,name, email, password)
            )
            print(f"User created! ID: {user_id}")
        except:
            print("User already exists or error occurred")

    def login(self):
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()

        if "@" not in email or not password:
            print("Invalid input")
            return

        try:
            user = self.user_service.login_user(email, password)

            if user:
                self.current_user = user
                print(f"Welcome {user.name}")
                self.user_dashboard()
            else:
                print("Invalid credentials")
        except:
            print("Login error")

    def user_dashboard(self):
        while True:
            print("\n====== DASHBOARD ======")
            print("1.Create Itinerary\n2.Add Item\n3.Book\n4.Expense\n5.Upcoming\n6.Total Expense\n7.Logout\n8.View Itineraries\n9.Delete Itinerary")

            choice = input("Enter choice: ").strip()

            try:
                if choice == "1":
                    self.create_itinerary()
                elif choice == "2":
                    self.add_item()
                elif choice == "3":
                    self.create_booking()
                elif choice == "4":
                    self.add_expense()
                elif choice == "5":
                    self.view_upcoming()
                elif choice == "6":
                    self.view_total_expense()
                elif choice == "7":
                    self.current_user = None
                    break
                elif choice == "8":
                    self.view_itineraries()
                elif choice == "9":
                    self.delete_itinerary()
                else:
                    print("Invalid choice")
            except Exception as e:
                print(f"Error: {e}")

    def create_itinerary(self):
        title = input("Title: ").strip()
        if not title:
            print("Invalid title")
            return

        itin_id = self.itinerary_service.create_itinerary(
            Itinerary(self.current_user.id, title)
        )
        print(f"Created ID: {itin_id}")

    def add_item(self):
        try:
            itin_id = int(input("Itinerary ID: "))
            name = input("Name: ").strip()
            desc = input("Desc: ").strip()
            date = input("Date (YYYY-MM-DD): ").strip()
            time = input("Time: ").strip()
            cost = float(input("Estimated Cost: "))

            datetime.strptime(date, "%Y-%m-%d")

            if not name:
                print("Invalid input")
                return

            self.itinerary_service.add_item(
                Item(itin_id, name, desc, date, time,cost)
            )
            print("Added")
        except Exception as e:
            print("Invalid data",e)

    def create_booking(self):
        try:
            b_type = input("Type: ").strip()
            details = input("Details: ").strip()
            date = input("Date: ").strip()
            cost = float(input("Cost: "))

            if not b_type or cost < 0:
                print("Invalid input")
                return

            self.booking_service.create_booking(
                Booking(self.current_user.id, b_type, details, date, cost)
            )
            print("Booked")
        except:
            print("Invalid booking")

    def add_expense(self):
        try:
            category = input("Category: ").strip()
            amount = float(input("Amount: "))
            date = input("Date: ").strip()

            if amount < 0:
                print("Invalid amount")
                return

            self.expense_service.add_expense(
                Expense(self.current_user[0], category, amount, date)
            )
            print("Added")
        except:
            print("Invalid expense")

    def view_upcoming(self):
        results = self.report_service.upcoming_items(self.current_user[0])
        print("\n--- Upcoming ---")
        if results:
            for r in results:
                print(r)
        else:
            print("No data")

    def view_total_expense(self):
        total = self.expense_service.total_expense(self.current_user[0])
        print(f"Total: {total if total else 0}")

    def view_itineraries(self):
        data = self.itinerary_service.get_user_itineraries(self.current_user.id)
        print("\n--- Itineraries ---")
        if data:
            for d in data:
                print(f"{d[0]} | {d[2]}")
        else:
            print("No data")

    def delete_itinerary(self):
        try:
            itin_id = int(input("Enter ID: "))
            self.itinerary_service.delete_itinerary(itin_id)
            print("Deleted")
        except:
            print("Invalid ID")


if __name__ == "__main__":
    app = TravelApp()
    app.run()
from data.database import DatabaseHandlder
from services.user_services import UserService
from services.habit_services import HabitService
from services.reward_services import RewardService
from models.user import User
from models.habit import Habit
class HabitTracker:
    def __init__(self):
        self.db = DatabaseHandlder()
        self.current_user = None
        self.user_service = UserService(self.db)
        self.habit_service = HabitService(self.db)
        self.reward_service = RewardService(self.db)
    def start_application(self):
        print("======= Welcome to Habit Tracker =======")
        self.show_main_menu()
    def show_main_menu(self):
        while True:
            print(" ----- MAIN MENU ----- ")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            try:
                choice = input("Enter Choice: ")
            except ValueError:
                print("❌ Invalid Input")
                continue

            if choice == '1':
                self.register_user()

            elif choice == '2':
                self.login_user()
                

            elif choice == '3':
                print("Exiting....")
                break
            else:
                print("Invalid choice")

    def user_menu(self):
        while True:
            print("\n----- USER MENU -----")
            print("1. Create Habit")
            print("2. View Habits")
            print("3. Mark Habit Complete")
            print("4. View Earned Rewards")
            print("5. View Available Rewards")
            print("6. Logout")

            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("❌ Invalid input. Enter a number")
                continue

            if choice == 1:
                self.create_habit()
            
            elif choice == 2:
                self.view_habit()
            
            elif choice == 3:
                self.mark_habit_complete()

            elif choice == 4:
                self.view_earned_rewards()

            elif choice == 5:
                self.view_available_rewards()

            elif choice == 6:
                print("Logged out")
                self.current_user = None
                break

            else:
                print("Invalid choice")

    def register_user(self):
        print(" ----- Register User -----")

        user_name = input("Enter Name: ")
        phone_no = input("Enter Phone Number: ")
        email_id = input("Enter Email id: ")
        password = input("Enter Password: ")
        reminder_time = input("Enter reminder Time (HH:MM:SS): ")
        
        try:
            self.user_service.register(user_name,email_id,phone_no,password,reminder_time)
            print("✅ User Registered Successfully.")
        except Exception as e:
            print("Error Found: ",e)

    def login_user(self):
        print("----- Login -----")

        email = input("Enter Email: ")
        password = input("Enter Password: ")

        user = self.user_service.login(email,password)
        if user:
            self.current_user = user
            print(f"\n✅ WELCOME, {self.current_user.name}!")
            print("Let's build your habits 💪\n")
            self.user_menu()   
        else:
            print("❌ Invalid Credentials")

    def create_habit(self):
        print("----- Create Habit -----")
        habit_name = input("Name Your Habit: ")

        # --- CATEGORY ---
        print("--- SELECT THE CATEGORY FOR YOUR HABIT")
        categories = self.habit_service.get_categories()
        category_ids = [cat.category_id for cat in categories]
        for cat in categories:
            print(f"{cat.category_id}. {cat.category_name}")
        try:
            category_id = int(input("Enter Category ID: "))
        except ValueError:
            print("❌ Invalid Input")
        if category_id not in category_ids:
            print("❌ Invalid Category ID")
            return

        # --- TEMPLATE --- 
        print("----- SELECT TEMPLATE FOR YOUR HABIT (OPTIONAL)")
        templates = self.habit_service.get_templates()
        template_ids = [temp.template_id for temp in templates]
        for temp in templates:
            print(f"{temp.template_id}. {temp.template_name}")
        template_input = input("Enter Template ID or press Enter to skip: ")
        template_id = int(template_input) if template_input else None
        if template_id not in template_ids:
            print("❌ Invalid Template ID")


        # --- FREQUENCY ---
        print("Select Frequency:")
        print("1. Daily")
        print("2. Weekly")
        print("3. Monthly")

        freq_choice = input("Enter choice: ")

        if freq_choice == '1':
            frequency = 'Daily'
        elif freq_choice == '2':
            frequency = 'Weekly'
        elif freq_choice == '3':
            frequency = 'Monthly'
        else:
            print("❌ Invalid frequency")
            return


        # --- OTHERS --- 
        goal = input("Enter Goal: ")
        description = input("Describe Your Habit: ")
        
        habit = Habit(
        user_id=self.current_user.user_id,
        habit_name=habit_name,
        template_id=template_id,
        category_id=category_id,
        description=description,
        goal=goal,
        frequency=frequency
        )

        self.habit_service.create_habit(habit)
        print(f"✅ HABIT CREATED SUCCESSFULLY")

    def view_habit(self):
        print("------ YOUR HABITS ------")
        habits = self.habit_service.get_user_habits(self.current_user.user_id)
        if habits:
            for i,habit in enumerate(habits,start=1):
                longest  = self.habit_service.get_longest_streak(habit.habit_id)
                current = self.habit_service.calculate_streak(habit.habit_id)
                print(f"""{i}. ID: {habit.habit_id} | Name: {habit.habit_name} | 🔥 Current Streak: {current} | 🔥 Longest Streak: {longest}""")

        else:
            print("-------- NO HABITS FOUND --------")

        

    def mark_habit_complete(self):
        print("------ LOG YOUR HABIT STATUS ------")
        self.view_habit()
        # ---- Habit ID ---- 
        try:
            habit_id = int(input("Enter Habit ID: "))
        except ValueError:
            print("❌ Invalid input")
        # --- Status ---
        try:
            status = int(input("Enter Status (0 - Not Completed), (1 - Completed)"))
        except ValueError:
            print("❌ Invalid input")
        if status not in (0,1):
            print("❌ Invalid Input")
            return
        try:
            points = self.habit_service.log_habit(habit_id,self.current_user.user_id,status,self.reward_service)
            print("✅ Log Updated Successfully")
        except Exception as e:
            if 'UNIQUE constraint' in str(e):
                print("⚠️ Already logged for today")
            else:
                print("❌ Error Found:", e)
        print("✅ Habit logged successfully +{points} added🎉")
    
    def view_earned_rewards(self):
        rewards = self.reward_service.get_user_rewards(self.current_user.user_id)
        if rewards:
            print(" 🏆 YOUR REWARDS: ")
        else:
            print("NO REWARDS TO VIEW, GO AND EARN ONE 💪🏿🔥")
            return
        if rewards:
            for r in rewards:
                print(f"- {r[0]}")
    
    def view_available_rewards(self):
        rewards = self.reward_service.get_available_rewards(self.current_user.user_id)

        print("\n 🎯 AVAILABLE REWARDS:")
        if rewards:
            for r in rewards:
                print(f"- {r.reward_id} ({r.reward_title})")
        else:
            print("All rewards unlocked!! 🔥")

            
if __name__ == "__main__":
    app = HabitTracker()
    app.start_application()

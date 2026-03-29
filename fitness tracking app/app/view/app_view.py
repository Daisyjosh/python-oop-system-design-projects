class AppView:
    def __init__(self, user_controller, activity_controller, goal_controller):
        self.user_controller = user_controller
        self.activity_controller = activity_controller
        self.goal_controller = goal_controller
        self.current_user = None

    def start(self):
        while True:
            print("\n1. Register\n2. Login\n3. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                print(self.user_controller.register(username, password))

            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                user = self.user_controller.login(username, password)

                if user:
                    self.current_user = user
                    self.dashboard()
                else:
                    print("Invalid credentials")

            elif choice == "3":
                break

    def dashboard(self):
        while True:
            print("\n1. Add Activity\n2. View Activities\n3. Set Goal\n4. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                act = input("Activity: ")
                dur = input("Duration: ")
                print(self.activity_controller.add_activity(self.current_user.user_id, act, dur))

            elif choice == "2":
                acts = self.activity_controller.view_activities(self.current_user.user_id)
                for a in acts:
                    print(a.activity_type, a.duration)

            elif choice == "3":
                target = input("Enter Goal: ")
                print(self.goal_controller.set_goal(self.current_user.user_id, target))

            elif choice == "4":
                break
from app.repository.user_repository import UserRepository
from app.repository.activity_repository import ActivityRepository
from app.repository.goal_repository import GoalRepository

from app.service.user_service import UserService
from app.service.activity_service import ActivityService
from app.service.goal_service import GoalService

from app.controller.user_controller import UserController
from app.controller.activity_controller import ActivityController
from app.controller.goal_controller import GoalController

from app.view.app_view import AppView


def main():
    user_repo = UserRepository()
    activity_repo = ActivityRepository()
    goal_repo = GoalRepository()

    user_service = UserService(user_repo)
    activity_service = ActivityService(activity_repo)
    goal_service = GoalService(goal_repo)

    user_controller = UserController(user_service)
    activity_controller = ActivityController(activity_service)
    goal_controller = GoalController(goal_service)

    view = AppView(user_controller, activity_controller, goal_controller)
    view.start()


if __name__ == "__main__":
    main()
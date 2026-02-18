from student import Student
from database import DatabaseHandler


class StudentManager:
    def __init__(self):
        self.db = DatabaseHandler()

    def add_student(self):
        roll_no = int(input("Enter Roll No: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        cgpa = float(input("Enter CGPA: "))
        quota = input("Enter Quota (Government/Management): ")
        year = int(input("Enter Year (1-4): "))
        department = input("Enter Department: ")

        student = Student(roll_no, first_name, last_name, cgpa, quota, year, department)
        self.db.insert_student(student)

    def display_all_students(self):
        students = self.db.fetch_all_students()
        if not students:
            print("No students found.")
        else:
            for student in students:
                print(student)

    def search_student(self):
        roll_no = int(input("Enter Roll No to search: "))
        student = self.db.search_student(roll_no)

        if student:
            print(student)
        else:
            print("Student not found.")

    def delete_student(self):
        roll_no = int(input("Enter Roll No to delete: "))
        self.db.delete_student(roll_no)

    def update_student(self):
        roll_no = int(input("Enter Roll No to update: "))
        student = self.db.search_student(roll_no)

        if not student:
            print("Student not found.")
            return

        print("Leave blank to keep current value.")

        first_name = input(f"First Name ({student.first_name}): ") or student.first_name
        last_name = input(f"Last Name ({student.last_name}): ") or student.last_name
        cgpa_input = input(f"CGPA ({student.cgpa}): ")
        cgpa = float(cgpa_input) if cgpa_input else student.cgpa
        quota = input(f"Quota ({student.quota}): ") or student.quota
        year_input = input(f"Year ({student.year}): ")
        year = int(year_input) if year_input else student.year
        department = input(f"Department ({student.department}): ") or student.department

        updated_student = Student(roll_no, first_name, last_name, cgpa, quota, year, department)
        self.db.update_student(updated_student)

    def close(self):
        self.db.close_connection()


def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.display_all_students()
        elif choice == '3':
            manager.search_student()
        elif choice == '4':
            manager.update_student()
        elif choice == '5':
            manager.delete_student()
        elif choice == '6':
            manager.close()
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
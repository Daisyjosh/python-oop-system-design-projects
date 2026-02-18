import sqlite3
from student import Student


class DatabaseHandler:
    def __init__(self):
        self.connection = sqlite3.connect("students.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_no INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            cgpa REAL NOT NULL,
            quota TEXT NOT NULL,
            year INTEGER NOT NULL,
            department TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def insert_student(self, student):
        try:
            self.cursor.execute("""
            INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                student.roll_no,
                student.first_name,
                student.last_name,
                student.cgpa,
                student.quota,
                student.year,
                student.department
            ))
            self.connection.commit()
            print("Student added to database successfully.")
        except sqlite3.IntegrityError:
            print("Roll number already exists in database.")

    def fetch_all_students(self):
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()

        students = []
        for row in rows:
            student = Student(*row)
            students.append(student)

        return students

    def search_student(self, roll_no):
        self.cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
        row = self.cursor.fetchone()

        if row:
            return Student(*row)
        return None

    def delete_student(self, roll_no):
        self.cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
        self.connection.commit()

        if self.cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Student deleted successfully.")

    def update_student(self, student):
        self.cursor.execute("""
        UPDATE students
        SET first_name = ?, last_name = ?, cgpa = ?, quota = ?, year = ?, department = ?
        WHERE roll_no = ?
        """, (
            student.first_name,
            student.last_name,
            student.cgpa,
            student.quota,
            student.year,
            student.department,
            student.roll_no
        ))
        self.connection.commit()

        if self.cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Student updated successfully.")

    def close_connection(self):
        self.connection.close()
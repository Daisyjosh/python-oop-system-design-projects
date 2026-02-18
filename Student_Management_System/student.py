class Student:
    def __init__(self, roll_no, first_name, last_name, cgpa, quota, year, department):
        self.roll_no = roll_no
        self.first_name = first_name
        self.last_name = last_name
        self.cgpa = cgpa
        self.quota = quota
        self.year = year
        self.department = department

    def __str__(self):
        return (
            f"Roll No: {self.roll_no}\n"
            f"Name: {self.first_name} {self.last_name}\n"
            f"Department: {self.department}\n"
            f"Year: {self.year}\n"
            f"CGPA: {self.cgpa}\n"
            f"Quota: {self.quota}\n"
            "-----------------------------"
        )
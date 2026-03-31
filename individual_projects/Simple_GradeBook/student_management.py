# LV 1st Student management

# Class Student:
#   Attributes:
#       name
#       student_id
#       grades (empty list)
#       optional grade_level
#   Methods:
#       add_grade(grade):
#           Append grade to grades list
#       calculate_average():
#           If grades list not empty:
#               return sum(grades)/len(grades)
#           Else:
#               return 0
#       get_letter_grade():
#           avg = calculate_average()
#           If avg >= 90: return "A"
#           Elif avg >= 80: return "B"
#           Elif avg >= 70: return "C"
#           Elif avg >= 60: return "D"
#           Else: return "F"
#       display_info():
#           Display name, ID, grades, average, letter grade


# Function add_new_student():
#   Input name
#   Input student_id
#   Optional input grade_level
#   Create new Student object
#   Add student to GradeBook (or list)
#   Display "Student added successfully!"

# Student Management

# Student class
# student_management.py

# student_management.py

# student_management.py
# student_management.py

class Student:
    def __init__(self, name, student_id, grade_level=None):
        self.name = name
        self.student_id = student_id
        self.grades = []
        self.grade_level = grade_level

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def get_letter_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Grades: {self.grades if self.grades else 'No grades available.'}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")
        print(f"Academic Status: {self.get_academic_status()}")
        if self.grade_level:
            print(f"Grade Level: {self.grade_level}")

    def get_academic_status(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "Honor Student"
        elif avg >= 70:
            return "Good Standing"
        else:
            return "At Risk"


def add_new_student(gradebook, csv_path="individual_projects/Simple_GradeBook/grade.csv"):
    # Local import to avoid circular import
    from grade_management import save_gradebook_to_csv

    name = input("Enter student name: ")
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid input. Student ID must be a number.")
        return

    grade_level = input("Enter grade level (optional, press enter to skip): ")
    grade_level = grade_level if grade_level else None

    new_student = Student(name, student_id, grade_level)
    gradebook.add_student(new_student)
    print("Student added successfully!")

    save_gradebook_to_csv(gradebook, csv_path)
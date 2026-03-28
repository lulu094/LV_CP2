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
class Student:
    def __init__(self, name, student_id, grade_level=None):
        self.name = name
        self.student_id = student_id
        self.grades = []
        self.grade_level = grade_level

    # Add a grade
    def add_grade(self, grade):
        self.grades.append(grade)

    # Calculate average
    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    # Get letter grade
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

    # Display student information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")
        if self.grade_level:
            print(f"Grade Level: {self.grade_level}")


# Function to add new student
def add_new_student(gradebook):
    name = input("Enter student name: ")
    
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid input. Student ID must be a number.")
        return

    grade_level = input("Enter grade level (optional, press enter to skip): ")
    grade_level = grade_level if grade_level else None

    # Create new Student object and add to gradebook
    new_student = Student(name, student_id, grade_level)
    gradebook.append(new_student)
    print("Student added successfully!")



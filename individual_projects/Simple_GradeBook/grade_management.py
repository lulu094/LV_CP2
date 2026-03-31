# LV 1st Grade Management
import csv

# Function add_grade_to_student():
#   Display list of students with ID and Name
#   Input student_id
#   Find student in GradeBook by ID
#   If student found:
#       Input grade
#       If 0 <= grade <= 100:
#           Call student.add_grade(grade)
#           Display "Grade added successfully!"
#           Display current average and letter grade
#       Else:
#           Display "Invalid grade. Enter 0-100."
#   Else:
#       Display "Student ID not found"

def add_grade_to_student(gradebook):
    # Display list of students with ID and Name
    print("List of students:")
    for student in gradebook.students:
        print(f"ID: {student.student_id}, Name: {student.name}")
    
    # Input student ID
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Find student in GradeBook
    student_found = None
    for student in gradebook:
        if student.student_id == student_id:
            student_found = student
            break
    
    if student_found:
        # Input grade
        try:
            grade = float(input("Enter grade (0-100): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        
        # Validate grade
        if 0 <= grade <= 100:
            student_found.add_grade(grade)
            print("Grade added successfully!")
            print(f"Current average: {student_found.calculate_average():.2f}")
            print(f"Letter grade: {student_found.get_letter_grade()}")
        else:
            print("Invalid grade. Enter 0-100.")
    else:
        print("Student ID not found.")    
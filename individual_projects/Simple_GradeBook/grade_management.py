# LV 1st Grade Management

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
# grade_management.py
# LV 1st Grade Management

# grade_management.py
# grade_management.py
import csv

def save_gradebook_to_csv(gradebook, csv_path="individual_projects/Simple_GradeBook/grade.csv"):
    with open(csv_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["student_id", "name", "grade_level", "grades"])
        for student in gradebook.students:
            grades_str = ",".join(map(str, student.grades))
            writer.writerow([student.student_id, student.name, student.grade_level, grades_str])


def add_grade_to_student(gradebook, csv_path="individual_projects/Simple_GradeBook/grade.csv"):
    if not gradebook.students:
        print("No students found.")
        return

    print("List of students:")
    for student in gradebook.students:
        print(f"ID: {student.student_id}, Name: {student.name}")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    student_found = next((s for s in gradebook.students if s.student_id == student_id), None)
    if not student_found:
        print("Student ID not found.")
        return

    try:
        grade = float(input("Enter grade (0-100): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 0 <= grade <= 100:
        student_found.add_grade(grade)
        print("Grade added successfully!")
        print(f"Current average: {student_found.calculate_average():.2f}")
        print(f"Letter grade: {student_found.get_letter_grade()}")
        save_gradebook_to_csv(gradebook, csv_path)
    else:
        print("Invalid grade. Enter 0-100.")
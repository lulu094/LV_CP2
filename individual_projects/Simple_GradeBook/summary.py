# LV 1st Summary

# Function view_student_record():
#   Input student_id
#   Find student by ID
#   If found: call student.display_info()
#   Else: display "Student not found"
    
# Function view_all_students():
#   For each student in GradeBook:
#       Display ID, Name, Average, Letter Grade

# Function class_summary():
#   total_students = number of students in GradeBook
#   highest_grade = max of all student averages
#   lowest_grade = min of all student averages
#   class_avg = average of all student averages
#   Display total_students, class_avg, highest_grade, lowest_grade

# View a single student record
def view_student_record(gradebook):
    student_id = int(input("Enter student ID: "))
    student_found = gradebook.find_student(student_id)

    if student_found:
        student_found.display_info()
    else:
        print("Student not found.")


# View all students
def view_all_students(gradebook):
    if not gradebook.students:
        print("No students found.")
        return

    for student in gradebook.students:
        avg = student.calculate_average()
        letter = student.get_letter_grade()
        print(f"ID: {student.student_id}, Name: {student.name}, Average: {avg:.2f}, Letter Grade: {letter}")
def class_summary(gradebook):
    total_students = len(gradebook.students)

    print(f"Total Students: {total_students}")
    print(f"Class Average: {gradebook.class_average():.2f}")
    print(f"Highest Average: {gradebook.highest_average():.2f}")
    print(f"Lowest Average: {gradebook.lowest_average():.2f}")
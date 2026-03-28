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
    student_found = None
    for student in gradebook:
        if student.student_id == student_id:
            student_found = student
            break
    if student_found:
        student_found.display_info()
    else:
        print("Student not found.")


# View all students
def view_all_students(gradebook):
    for student in gradebook:
        avg = student.calculate_average()
        letter = student.get_letter_grade()
        print(f"ID: {student.student_id}, Name: {student.name}, Average: {avg:.2f}, Letter Grade: {letter}")


# Class summary
def class_summary(gradebook):
    total_students = len(gradebook)
    averages = [student.calculate_average() for student in gradebook]
    highest_grade = max(averages) if averages else 0
    lowest_grade = min(averages) if averages else 0
    class_avg = sum(averages)/total_students if total_students > 0 else 0

    print(f"Total Students: {total_students}")
    print(f"Class Average: {class_avg:.2f}")
    print(f"Highest Average: {highest_grade:.2f}")
    print(f"Lowest Average: {lowest_grade:.2f}")
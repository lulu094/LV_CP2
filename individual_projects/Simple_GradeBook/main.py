# LV 1st Simple Grade Book - Main

# dictionary with choices
# [1] Add New Student
# [2] Add Grade to Student
# [3] View Student Record
# [4] View All Students
# [5] Class Summary
# [6] Exit

choices = {
[1] = "Add New Student",
[2] = "Add Grade to Student",
[3] = "View Student Record",
[4] = "View All Students",
[5] = "Class Summary",
[6] = "Exit"
}

# function main
# Welcome
# Ask user to choose from choices
# if choice == 1
# take user to add new student
# elif choice == 2
# take user to add grade to student
# elif choice == 3
# take user to view all student record
# elif choice == 4
# take user to view all students
# elif choice == 5
# take user to class summary
# elif choice == 6
# exit
# Goodbye thank you for using simple grade !!!
# Would you like to use simple grade book y/n:
# else
# display Invalid input

# call main

def main():
    if choice == 1:
        add_new_student()
    elif choice == 2:
        grade_student()
    elif choice == 3:
        view_all_student_record()
    elif choice == 4:
        view_all_students()
    elif choice == 5:
        class_summary()
    elif choice == 6:
        exit
        print("Goodbye thank you for using simple grade !!!")
        print("# Would you like to use simple grade book y/n:")
    else
        print("Invalid input")

    
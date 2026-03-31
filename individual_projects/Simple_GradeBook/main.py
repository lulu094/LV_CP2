# LV 1st Simple Grade Book - Main

# dictionary with choices
# [1] Add New Student
# [2] Add Grade to Student
# [3] View Student Record
# [4] View All Students
# [5] Class Summary
# [6] Exit



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
    gradebook = GradeBook()
    
    print("Welcome to Simple Grade Book!")
    
    while True:
        # Display menu
        print("\nChoose an option:")
        print("[1] Add New Student")
        print("[2] Add Grade to Student")
        print("[3] View Student Record")
        print("[4] View All Students")
        print("[5] Class Summary")
        print("[6] Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_new_student(gradebook)
        elif choice == "2":
            add_grade_to_student(gradebook)
        elif choice == "3":
            view_student_record(gradebook)
        elif choice == "4":
            view_all_students(gradebook)
        elif choice == "5":
            class_summary(gradebook)
        elif choice == "6":
            print("Goodbye! Thank you for using Simple Grade Book!")
            again = input("Would you like to use Simple Grade Book again? (y/n): ").lower()
            if again == "y":
                continue
            else:
                break
        else:
            print("Invalid input. Please choose a number from 1 to 6.")


# Call main to run the program
main()   
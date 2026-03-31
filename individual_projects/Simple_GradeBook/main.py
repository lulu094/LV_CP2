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
# LV 1st Simple Grade Book - Main

# LV 1st Simple Grade Book - Main

# main.py
# main.py - Simple Grade Book

import csv
from student_management import add_new_student, Student
from grade_management import add_grade_to_student, save_gradebook_to_csv
from gradebook import GradeBook
from summary import view_student_record, view_all_students, class_summary

# CSV file path
CSV_PATH = "individual_projects/Simple_GradeBook/grade.csv"

# Initialize GradeBook
gradebook = GradeBook()

# Load existing students from CSV
def load_gradebook_from_csv(csv_path):
    try:
        with open(csv_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_id = int(row["student_id"])
                name = row["name"]
                grade_level = row["grade_level"] if row["grade_level"] != "" else None
                grades = list(map(float, row["grades"].split(","))) if row["grades"] else []

                student = Student(name, student_id, grade_level)
                student.grades = grades
                gradebook.add_student(student)
    except FileNotFoundError:
        print("No existing grade file found. Starting fresh.")

# Load data at startup
load_gradebook_from_csv(CSV_PATH)

# Main program
def main():
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
            add_new_student(gradebook, CSV_PATH)  # Save immediately after adding
        elif choice == "2":
            add_grade_to_student(gradebook, CSV_PATH)  # Save immediately after adding
        elif choice == "3":
            view_student_record(gradebook)
        elif choice == "4":
            view_all_students(gradebook)
        elif choice == "5":
            class_summary(gradebook)
        elif choice == "6":
            print("Goodbye! Thank you for using Simple Grade Book!")
            break
        else:
            print("Invalid input. Please choose a number from 1 to 6.")

# Run the program
main()
# Simple Grade Book
LV 1st Simple Grade Book

## Overview

This Python program allows users to manage student records, including adding new students, recording grades, and viewing class summaries. The program stores all student data in a CSV file for persistence.

The program allows the user to:
- Add new students with optional grade level
- Add grades to existing students
- View individual student records
- View all students in the class
- Generate a class summary with averages and letter grades
- Save and load data from a CSV file

## Project Structure

- main.py → Handles user interaction and runs the program  
- student_management.py → Contains the Studen` class and functions to add new students  
- grade_management.py → Functions to add grades and save/load CSV data  
- gradebook.py → Contains the GradeBook class for storing students  
- summary.py → Functions for viewing individual or all student records and class summaries  
- README.md → Project description  

## How It Works

1. **Add New Student:** Prompts for name, ID, and optional grade level. Saves the student to the CSV file.  
2. **Add Grade to Student:** Displays all students and allows entry of a numeric grade (0–100). Updates the CSV immediately.  
3. **View Student Record:** Displays name, ID, grades, average, letter grade, and academic status for a selected student.  
4. **View All Students:** Lists all students with their basic details.  
5. **Class Summary:** Shows overall class averages, letter grades, and academic statuses.

Grades are calculated automatically, and each student is assigned a letter grade:
- A: 90–100
- B: 80–89
- C: 70–79
- D: 60–69
- F: 0–59

Students with an average ≥ 90 are labeled **Honor Student**, 70–89 are **Good Standing**, and below 70 are **At Risk**.

## Concepts Used

- Object-Oriented Programming (Student and GradeBook classes)  
- CSV for saving/loading data  
- Input validation  
- Functional decomposition  
- Loops and conditionals for menu-driven programs  

## How to Run

1. Make sure Python is installed.  
2. Go to the project folder containing main.p`.  
3. Run the program in terminal:

## Author
lulu094
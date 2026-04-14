# Personal Portfolio 
LV 1st Personal Portfolio

## Overview

This Python program is a graphical user interface (GUI) portfolio that allows users to navigate and run multiple coding projects from one main menu. Each project opens in a separate window and includes a description before the code is executed.

The program allows the user to:
- Navigate a main menu with buttons for each project
- Open different project windows using Tkinter
- Read project descriptions before running any code
- Run projects through GUI buttons
- Save project results to a CSV file
- Organize multiple Python files in one system


## Project Structure

- main.py - Main menu that connects all projects
- calculator.py - Calculator project GUI
- user_input.py - User input processing project GUI
- data_tracker.py - Data tracker project GUI
- individual_projects/portafolio/data.csv - Stores project run results


## How It Works

1. Main Menu:
   The program starts with a main GUI window that has buttons for each project.

2. Opening Projects:
   Clicking a button opens a new window for that project.

3. Project Information:
   Each project displays:
   - What the project does
   - What I learned
   - A challenge I overcame  
   This information appears before running the project.

4. Running Projects:
   Each project has a run button that executes the program and displays a success message.

5. Saving Data:
   When a project is run, it writes the result into:
   individual_projects/portafolio/data.csv

6. File Organization:
   Each project is separated into its own Python file and connected through imports in the main menu.


## Concepts Used

- Tkinter GUI development
- Object-Oriented Programming (classes)
- File handling (CSV writing)
- Event handling (button clicks)
- Modular programming using multiple files



## Requirements for Code to Run

- Python installed
- Tkinter installed 
- All project files in the same folder


## Author
lulu094
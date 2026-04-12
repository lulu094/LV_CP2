# ================================
# PROJECT 1 PAGE - PSEUDOCODE
# ================================

# import tkinter as tk
# from tkinter import ttk

# PURPOSE:
# This page displays Project 1 information and allows the user to read
# about the project BEFORE running it from the portfolio GUI.

# class Project1Page:
#     def __init__(self, root):
#         # initialize main window frame for project 1
#         # create main_frame to hold all widgets
#         # set window title to "Project 1"
#
#         # create title label (Project 1 Name)
#         # create text box / label area for project description
#
#         # DESCRIPTION CONTENT (display BEFORE code runs):
#         # what project does:
#         # - explain functionality in 1–2 sentences
#
#         # what I learned:
#         # - bullet 1
#         # - bullet 2
#
#         # challenge overcome:
#         # - one programming challenge and how it was solved
#
#         # create "Run Project" button
#         # button should call self.run_project when clicked
#
#     def run_project(self):
#         # EVENT HANDLER:
#         # this function launches the actual Project 1 program
#         # use subprocess or import-based integration
#         # include error handling if file path is incorrect
#
#     def show_info(self):
#         # updates GUI text area with project description
#         # ensures info is shown BEFORE project execution
# ================================
# PROJECT 1 PAGE
# ================================

# ================================
# PROJECT 1 PAGE
# ================================

import tkinter as tk
import csv
import os


class Project1Page:
    def __init__(self, root):
        self.root = root
        self.root.title("Project 1")

        # Title
        tk.Label(root, text="Project 1", font=("Arial", 14)).pack(pady=10)

        # Description (SHOWN BEFORE RUNNING)
        self.info = tk.Text(root, height=10, width=60)
        self.info.pack()

        self.info.insert(tk.END,
            "What it does:\n"
            "- This project demonstrates basic Python logic.\n\n"
            "What I learned:\n"
            "- Tkinter GUI structure\n"
            "- Button event handling\n\n"
            "Challenge:\n"
            "- Managing multiple windows\n"
        )

        # Run Button
        tk.Button(root, text="Run Project 1", command=self.run_project).pack(pady=10)

    def run_project(self):

        # make sure folder exists
        os.makedirs("individual_projects/portafolio", exist_ok=True)

        file_path = "individual_projects/portafolio/data.csv"

        # write to CSV
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Project 1", "Ran successfully"])

        # show result in GUI
        tk.Label(self.root, text="Project 1 executed!", fg="green").pack()
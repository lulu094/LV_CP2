# ================================
# PROJECT 3 PAGE - PSEUDOCODE
# ================================

# import tkinter as tk
# from tkinter import ttk

# PURPOSE:
# This page displays Project 3 details and allows execution from GUI
# after the user reads the description.

# class Project3Page:
#     def __init__(self, root):
#         # initialize Project 3 frame
#         # set window title "Project 3"
#
#         # create heading label for project name
#
#         # create description box:
#         # must include:
#         # - what project does (1–2 sentences)
#         # - what I learned (2 bullet points)
#         # - challenge overcome (1 bullet point)
#
#         # create button labeled "Run Project 3"
#         # button triggers self.run_project_3
#
#     def run_project_3(self):
#         # EVENT HANDLER:
#         # runs Project 3 script
#         # ensure correct file linking
#         # handle missing file errors gracefully
#
#     def load_project_info(self):
#         # ensures project info is displayed FIRST
#         # populates GUI text widget with description content
# ================================
# PROJECT 3 PAGE
# ================================

# ================================
# PROJECT 3 PAGE
# ================================

import tkinter as tk
import csv
import os


class Project3Page:
    def __init__(self, root):
        self.root = root
        self.root.title("Project 3")

        tk.Label(root, text="Project 3", font=("Arial", 14)).pack(pady=10)

        self.info = tk.Text(root, height=10, width=60)
        self.info.pack()

        self.info.insert(tk.END,
            "What it does:\n"
            "- This project simulates a simple application system.\n\n"
            "What I learned:\n"
            "- File handling\n"
            "- GUI navigation\n\n"
            "Challenge:\n"
            "- Organizing multiple functions cleanly\n"
        )

        tk.Button(root, text="Run Project 3", command=self.run_project).pack(pady=10)

    def run_project(self):

        result = "Project 3 executed successfully!"

        # make sure folder exists
        os.makedirs("individual_projects/portafolio", exist_ok=True)

        file_path = "individual_projects/portafolio/data.csv"

        # write to CSV
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Project 3", result])

        # show result in GUI
        tk.Label(self.root, text=result, fg="green").pack()
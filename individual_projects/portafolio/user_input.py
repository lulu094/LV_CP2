# User Input Page 

# import tkinter as tk
# from tkinter import ttk

# PURPOSE:
# This page provides a GUI interface for Project 2 and shows a full
# description before allowing the user to run the project.

# class Project2Page:
#     def __init__(self, root):
#         # create frame for Project 2
#         # set title label: "Project 2"
#
#         # create description display area (label or text widget)
#
#         # PROJECT DESCRIPTION (must show before run):
#         # what project does:
#         # - 1–2 sentence explanation
#
#         # what I learned:
#         # - concept 1
#         # - concept 2
#
#         # challenges:
#         # - one specific challenge and fix
#
#         # create button: "Launch Project 2"
#         # assign command -> self.launch_project
#
#     def launch_project(self):
#         # EVENT HANDLER:
#         # opens Project 2 file
#         # ensure correct file path integration
#         # include try/except for safety
#
#     def update_description(self):
#         # updates the text area with project details
#         # ensures user reads info before execution


import tkinter as tk
import csv
import os


class UserInput:
    def __init__(self, root):
        self.root = root
        self.root.title("User Input")  

        tk.Label(root, text="User Input Project", font=("Arial", 14)).pack(pady=10)

        self.info = tk.Text(root, height=10, width=60)
        self.info.pack()

        self.info.insert(tk.END,
            "What it does:\n"
            "- This project performs user input processing.\n\n"
            "What I learned:\n"
            "- Conditionals and loops\n"
            "- GUI input handling\n\n"
            "Challenge:\n"
            "- Validating user input\n"
        )

        tk.Button(root, text="Run Project 2", command=self.run_project).pack(pady=10)

    def run_project(self):
        result = "Project 2 executed successfully!"

        # ✔ correct folder path
        os.makedirs("individual_projects/portafolio", exist_ok=True)

        file_path = "individual_projects/portafolio/data.csv"

        # ✔ write to correct CSV
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Project 2", result])

        tk.Label(self.root, text=result, fg="green").pack()
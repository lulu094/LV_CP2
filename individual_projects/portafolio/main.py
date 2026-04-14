# LV 1st Main

# import tkinter as tk
# from tkinter import ttk

# class PortfolioApp:
#     def __init__(self, root):
#         # store root window
#         # set title: "Personal Portfolio"
#         # set window size (example: 800x600)
#
#         # create main frame (container for all widgets)
#
#        
#         # INTRODUCTION SECTION
#       
#         # create label: "Welcome to My Programming Portfolio"
#
#         # create instruction label:
#         # "Click a project button below to view details and run the project.
#         # Each project shows a description before execution."
#
#         # PROJECT BUTTON SECTION
#
#         # create button: Project 1
#         # name: project1_btn
#         # command: self.open_project1
#
#         # create button: Project 2
#         # name: project2_btn
#         # command: self.open_project2
#
#         # create button: Project 3
#         # name: project3_btn
#         # command: self.open_project3
#
#         # create button: Exit
#         # command: root.quit
#
#     
#     # EVENT HANDLERS
#
#     def open_project1(self):
#         # open new window (tk.Toplevel)
#         # call Project1Page(new_window)
#         # ensures project info loads BEFORE execution button is used
#
#     def open_project2(self):
#         # open new window (tk.Toplevel)
#         # call Project2Page(new_window)
#
#     def open_project3(self):
#         # open new window (tk.Toplevel)
#         # call Project3Page(new_window)


from logging import root
import tkinter as tk

from calculator import Calculator
from data_tracker import DataTracker
from user_input import UserInput

# MAIN MENU FUNCTION
def menu():
    root = tk.Tk()
    root.title("Personal Portfolio")
    root.geometry("600x400")

    # Title
    title = tk.Label(root, text="My Programming Portfolio", font=("Arial", 16))
    title.pack(pady=10)

    # Instructions
    instructions = tk.Label(
        root,
        text="Click a project to view details BEFORE running it.",
        wraplength=500
    )
    instructions.pack(pady=10)

  
    # BUTTONS

    def open_project1():
        win = tk.Toplevel(root)
        Calculator(win)

    def open_project2():
        win = tk.Toplevel(root)
        UserInput(win)

    def open_project3():
        win = tk.Toplevel(root)
        DataTracker(win)

    tk.Button(root, text="Project 1", width=20, command=open_project1).pack(pady=5)
    tk.Button(root, text="Project 2", width=20, command=open_project2).pack(pady=5)
    tk.Button(root, text="Project 3", width=20, command=open_project3).pack(pady=5)

    tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=20)

    root.mainloop()



menu()
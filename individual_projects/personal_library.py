# LV 1st Peronal Library
# Main Program
# Start program
# Call main_menu()
"""Stores all items in a list
Function to add a new item
Function to search the items
Function to remove an item
Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)
Project must include
easy to understand variable and function names
Pseudocode comments explaining what the code is doing
Good use of white space to keep items separate and easy to read/find
Have at least 2 people test your code before submission!"""
# make a tuple in the main proram run while loop
# List to store library items
# Each item is represented as a dictionary with 'title' and 'author' keys
# Initialize an empty list to store library items
library_items = []
# Function to display the main menu and get user choice
# This function shows the available options to the user and returns their choice
def main_menu():
    print("\nPersonal Library Menu:")
    print("1. View all items")
    print("2. Add a new item")
    print("3. Remove an item")
    print("4. Search for an item")
    print("5. Exit")
    choice = int(input("Please enter your choice (1-5): ")) # make sure it is a #, so it doesn't crahs out!!!!
    return choice
# Function to view all items in the library
# This function prints all the items currently stored in the library
# If there are no items, returns to the main menu
# Ennumarate how many items there are
# Loop back to main menu
def view_items():
    if not library_items:
        print("No items in the library.")
    else:
        print("\nLibrary Items:")
        for index, item in enumerate(library_items, start=1):
            print(f"{index}. Title: {item['title']}, Author: {item['author']}")
        return main_menu()

# Function add a new item to the library
# This function - the user for item details and adds it to the library list
# If the user inputs empty strings, it will not add the item
#Show you have aedded the item
# they have to loop again to the main menu
def add_item():
    title = input("Enter the title of the item: ")
    author = input("Enter the author of the item: ")
    if title and author:
        library_items.append({'title': title, 'author': author})
        print(f"Item '{title}' by {author} added to the library.")
    else:
        print("Title and Author cannot be empty.")

# Function to remove an item from the library
# This function - the user for the title of the item to remove
# If the item is found, it is removed from the list
# else print item not found
# return to main menu

# Function search for an item in the library
#Start program
main_menu()
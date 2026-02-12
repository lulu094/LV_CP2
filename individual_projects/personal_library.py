# LV 1st Personal Project and Update Personal Library

# Update Personal Library Pseudocode
# Need dictionaries with each library item and have tuples
# Changes and books have to be saved in a txt file "library.txt"
# The main menu will have more options
# Show simple list
# Show detailed list
# Add item
# Update item
# Delete item
# Save library
# Reload library from file
# Exit (prompt to save if changes)


# then show
# Title:
# Creator (author/artist/director):
# Year:
# Genre:
# Optional: format, rating, notes

# keep the main code of the personal library just update it witht the new requirements
# when showing simple library
# 
# when showing detailed list
#
# Reload - just restart with the list with the original list

# when exiting make sure to ask the user if they want to save their changes and if they want to do it again once said godbye
# 

# Personal Library Pseudocode

# allows a user to manage a book collection

# create a list to store books
# display a menu inside a while true loop
# ask the user what they want to do
# call the correct function
# exit only when the user chooses exit

# tuple for menu options
menuoptions = (
    "View all books",
    "Add a book",
    "Remove a book",
    "Search for a book",
    "Exit"
)

# list to store the library books
library = [
    {"title": "The Hobbit", "author": "J.R.R Tolkien"},
    {"title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
    {"title": "Steelheart", "author": "Brandon Sanderson"},
    {"title": "The Giver", "author": "Lois Lowry"},
    {"title": "Fablehaven", "author": "Brandon Mull"}
]


# define function display_menu
#     display menu instructions
#     loop through menu options
#     display option number and text
def displaymenu():
    """Displays the main menu"""
    print("\nType the number for the action you would like to perform:")
    for index, option in enumerate(menuoptions, start=1):
        print(f"{index}. {option}")

# define function view_books
#     if library is empty
#         display "library is empty"
#     else
#         loop through library
#         display each book's title and author
def viewbooks():
    """Displays all books in the library"""
    if not library:
        print("\nYour library is empty.")
        return

    print("\nYour Library:")
    for title, author in library:
        print(f"{title} by {author}")

# define function add_book
#     ask user for book title
#     ask user for author name
#     add new book to library
#     display confirmation message
def addbook():
    """Adds a new book to the library"""
    print("\nAdd a New Book")
    title = input("Title: ").strip()
    author = input("By: ").strip()

    library.append((title, author))
    print(f"\nYou have added:\n{title} by {author}")

# define function remove_book
#     if library is empty
#         display "no books to remove"
#         return
#     display numbered list of books
#     ask user to choose a book number
#     if choice is invalid
#         display error message
#     else
#         remove selected book from library
#         display confirmation message
def removebook():
    """Removes a book chosen by number"""
    if not library:
        print("\nNo books to remove.")
        return

    print("\nSelect a book to remove:")
    for index, (title, author) in enumerate(library, start=1):
        print(f"{index}. {title} by {author}")

    choice = input("Enter the number of the item you would like to remove: ")

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(library):
        print("Invalid selection.")
        return

    removedBook = library.pop(int(choice) - 1)
    print(f"\nYou have removed {removedBook[0]} by {removedBook[1]}")

# define function search_books
#     display search options (title or author)
#     ask user for choice
#     if searching by title
#         ask for title keyword
#         loop through library
#         if keyword is in book title
#             display book
#     else if searching by author
#         ask for author name
#         loop through library
#         if name is in book author
#             display book
#     else
#         display invalid option message
def searchbooks():
    """Searches books by title or author"""
    print("\nWhat would you like to search by?")
    print("1. Title")
    print("2. Author")

    choice = input("Choice: ")

    if choice == "1":
        searchTerm = input("Enter title keyword: ").lower()
        for title, author in library:
            if searchTerm in title.lower():
                print(f"{title} by {author}")

    elif choice == "2":
        searchTerm = input("Enter author's name: ").lower()
        for title, author in library:
            if searchTerm in author.lower():
                print(f"{title} by {author}")

    else:
        print("Invalid search option.")

# main program loop

# display welcome message

# while program is running
#     call display_menu
#     ask user for menu choice
#     if choice is 1
#         call view_books
#     else if choice is 2
#         call add_book
#     else if choice is 3
#         call remove_book
#     else if choice is 4
#         call search_books
#     else if choice is 5
#         display goodbye message
#         exit loop
#     else
#         display invalid choice message
print("Welcome to the Personal Library Program!")

while True:
    displaymenu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        viewbooks()
    elif choice == "2":
        addbook()
    elif choice == "3":
        removebook()
    elif choice == "4":
        searchbooks()
    elif choice == "5":
        print("\nGoodbye! Thanks for using the library.")
        break
    else:
        print("Invalid option. Please try again.")
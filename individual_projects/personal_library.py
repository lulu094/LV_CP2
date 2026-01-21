# LV 1st Personal Project
# allows a user to manage a book collection

# create a list to store books
# display a menu inside a while true loop
# ask the user what they want to do
# call the correct function
# exit only when the user chooses exit

# tuple for menu options
menuOptions = (
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
def displayMenu():
    """Displays the main menu"""
    print("\nType the number for the action you would like to perform:")
    for index, option in enumerate(menuOptions, start=1):
        print(f"{index}. {option}")

# define function view_books
#     if library is empty
#         display "library is empty"
#     else
#         loop through library
#         display each book's title and author
def viewBooks():
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
def addBook():
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
def removeBook():
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
def searchBooks():
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
    displayMenu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        viewBooks()
    elif choice == "2":
        addBook()
    elif choice == "3":
        removeBook()
    elif choice == "4":
        searchBooks()
    elif choice == "5":
        print("\nGoodbye! Thanks for using the library.")
        break
    else:
        print("Invalid option. Please try again.")
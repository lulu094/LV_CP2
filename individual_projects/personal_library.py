# -----------------------------------------
# personal_library_program
# allows a user to manage a book collection
# -----------------------------------------

# PSEUDOCODE:
# create a list to store books
# display a menu inside a while true loop
# ask the user what they want to do
# call the correct function
# exit only when the user chooses exit

# tuple for menu options
menu_options = (
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


def display_menu():
    """displays the main menu"""
    print("\nType the number for the action you would like to perform:")
    for index, option in enumerate(menu_options, start=1):
        print(f"{index}. {option}")


def view_books():
    """displays all books in the library"""
    if not library:
        print("\nYour library is empty.")
        return

    print("\nYour Library:")
    for book in library:
        print(f"{book['title']} by {book['author']}")


def add_book():
    """adds a new book to the library"""
    print("\nAdd a New Book")
    title = input("Title: ").strip()
    author = input("By: ").strip()

    library.append({"title": title, "author": author})

    print(f"\nYou have added:\n{title} by {author}")


def remove_book():
    """removes a book chosen by number"""
    if not library:
        print("\nNo books to remove.")
        return

    print("\nSelect a book to remove:")
    for index, book in enumerate(library, start=1):
        print(f"{index}. {book['title']} by {book['author']}")

    choice = input("Enter the number of the item you would like to remove: ")

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(library):
        print("Invalid selection.")
        return

    choice = int(choice)
    removed_book = library.pop(choice - 1)

    print(f"\nYou have removed {removed_book['title']} by {removed_book['author']}")


def search_books():
    """searches books by title or author"""
    print("\nWhat would you like to search by?")
    print("1. Title")
    print("2. Author")

    choice = input("Choice: ")

    if choice == "1":
        search_term = input("Enter title keyword: ").lower()
        for book in library:
            if search_term in book["title"].lower():
                print(f"{book['title']} by {book['author']}")

    elif choice == "2":
        search_term = input("Enter author's name: ").lower()
        for book in library:
            if search_term in book["author"].lower():
                print(f"{book['title']} by {book['author']}")

    else:
        print("Invalid search option.")


# -----------------------
# main program loop
# -----------------------

print("Welcome to the Personal Library Program!")

while True:
    display_menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        view_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        remove_book()
    elif choice == "4":
        search_books()
    elif choice == "5":
        print("\nGoodbye! Thanks for using the library.")
        break
    else:
        print("Invalid option. Please try again.")

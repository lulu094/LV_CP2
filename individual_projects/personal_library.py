# LV 1st Personal Project and Update Personal Library

# Persoanl Library

# allows a user to manage a book collection
# create a list to store books
# display a menu inside a while true loop
# ask the user what they want to do
# call the correct function
# exit only when the user chooses exit


# UPDATE PERSONAL LIBRARY 


# library must now be a list of dictionaries
# each dictionary contains:
# title, creator, year, genre, format, rating, notes

# data must be saved to:
# individual_projects/library.txt

# when program starts:
#     load library from file
#     if file does not exist:
#         create it

# menu must include:
# show simple list (title + creator)
# show detailed list (all fields)
# add item
# update item
# delete item
# save library
# reload library from file
# exit (ask to save if unsaved changes)

# file format per line:
# title|creator|year|genre|format|rating|notes


import os

file_path = "individual_projects/library.txt"


def load_library(path):
    """Load the library from file. Create file if it does not exist."""
    library = []
    os.makedirs("individual_projects", exist_ok=True)

    if not os.path.exists(path):
        open(path, "w").close()
        return library

    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 7:
                try:
                    library.append({
                        "title": parts[0],
                        "creator": parts[1],
                        "year": int(parts[2]),
                        "genre": parts[3],
                        "format": parts[4],
                        "rating": parts[5],
                        "notes": parts[6]
                    })
                except ValueError:
                    print("Warning: Skipping invalid row.")
            else:
                print("Warning: Skipping malformed row.")

    return library


def save_library(path, library):
    """Save the library to file."""
    with open(path, "w") as file:
        for item in library:
            line = "|".join([
                item["title"],
                item["creator"],
                str(item["year"]),
                item["genre"],
                item["format"],
                item["rating"],
                item["notes"]
            ])
            file.write(line + "\n")
    print("Library saved successfully.")


def show_simple(library):
    """Display library with only title and creator."""
    if not library:
        print("Library is empty.")
        return
    for index, item in enumerate(library, start=1):
        print(f"{index}. {item['title']} by {item['creator']}")


def show_detailed(library):
    """Display all fields of each item in the library."""
    if not library:
        print("Library is empty.")
        return
    for index, item in enumerate(library, start=1):
        print(f"\nIndex: {index}")
        for key, value in item.items():
            print(f"{key.capitalize()}: {value}")


def add_item(library):
    """Add a new item to the library."""
    print("\nAdd a New Item")
    title = input("Title: ").strip()
    creator = input("Creator (author/artist/director): ").strip()

    while True:
        year_input = input("Year: ").strip()
        if year_input.isdigit():
            year = int(year_input)
            break
        print("Invalid year. Please enter a number.")

    genre = input("Genre: ").strip()
    format_type = input("Format (optional): ").strip()
    rating = input("Rating (optional): ").strip()
    notes = input("Notes (optional): ").strip()

    library.append({
        "title": title,
        "creator": creator,
        "year": year,
        "genre": genre,
        "format": format_type,
        "rating": rating,
        "notes": notes
    })
    print("Item added successfully.")
    return True


def update_item(library):
    """Update an existing item."""
    show_simple(library)
    if not library:
        return False

    choice = input("Enter number of item to update: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(library):
        print("Invalid selection.")
        return False

    item = library[int(choice) - 1]
    print("Press Enter to keep current value.")

    for key in item:
        new_value = input(f"{key.capitalize()} ({item[key]}): ")
        if new_value:
            if key == "year":
                if new_value.isdigit():
                    item[key] = int(new_value)
                else:
                    print("Invalid year. Keeping old value.")
            else:
                item[key] = new_value
    print("Item updated successfully.")
    return True


def delete_item(library):
    """Delete an item from the library."""
    show_simple(library)
    if not library:
        return False

    choice = input("Enter number of item to delete: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(library):
        print("Invalid selection.")
        return False

    removed = library.pop(int(choice) - 1)
    print(f"Removed {removed['title']}.")
    return True


def search_items(library):
    """Search items by title or creator."""
    print("\nSearch by:")
    print("1. Title")
    print("2. Creator")
    choice = input("Choice: ")

    if choice == "1":
        keyword = input("Enter title keyword: ").lower()
        found = False
        for item in library:
            if keyword in item["title"].lower():
                print(f"{item['title']} by {item['creator']}")
                found = True
        if not found:
            print("No items found.")
    elif choice == "2":
        keyword = input("Enter creator keyword: ").lower()
        found = False
        for item in library:
            if keyword in item["creator"].lower():
                print(f"{item['title']} by {item['creator']}")
                found = True
        if not found:
            print("No items found.")
    else:
        print("Invalid choice.")


def display_menu(menu_options):
    """Display the main menu."""
    print("\nType the number for the action you would like to perform:")
    for index, option in enumerate(menu_options, start=1):
        print(f"{index}. {option}")


# Main program loop

menu_options = (
    "Show simple list",
    "Show detailed list",
    "Add item",
    "Update item",
    "Delete item",
    "Save library",
    "Reload library from file",
    "Exit"
)

library = load_library(file_path)
unsaved_changes = False

print("Welcome to the Personal Library Program!")

while True:
    display_menu(menu_options)
    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        show_simple(library)
    elif choice == "2":
        show_detailed(library)
    elif choice == "3":
        if add_item(library):
            unsaved_changes = True
    elif choice == "4":
        if update_item(library):
            unsaved_changes = True
    elif choice == "5":
        if delete_item(library):
            unsaved_changes = True
    elif choice == "6":
        save_library(file_path, library)
        unsaved_changes = False
    elif choice == "7":
        if unsaved_changes:
            save_prompt = input("Unsaved changes will be lost. Continue? (y/n): ").lower()
            if save_prompt != "y":
                continue
        library = load_library(file_path)
        unsaved_changes = False
    elif choice == "8":
        if unsaved_changes:
            save_prompt = input("Save changes before exiting? (y/n): ").lower()
            if save_prompt == "y":
                save_library(file_path, library)
        print("Goodbye! Thanks for using the library.")
        break
    else:
        print("Invalid option. Please try again.")

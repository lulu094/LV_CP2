# LV 1st Word Counter - main.py 


# import view_document from file_handling
# import add_content_to_document from file_handling
# import update_document_info from file_handling

# define function display_menu()
    # print "--- Document Word Count Updater ---"
    # print "1. Update document info"
    # print "2. View document"
    # print "3. Add content to document"
    # print "4. Exit"

def display_menu():
    print "--- Document Word Count Updater ---"
    print "1. Update document info"
    print "2. View document"
    print "3. Add content to document"
    print "4. Exit"

# define function main()
def main():
    # create variable document_path
    # set document_path equal to empty string
    document_path = ""

    # create variable user_choice
    # set user_choice equal to 0
    user_choice = 0

    # start while loop that runs until user_choice equals 4
    while user_choice != 4:
        # call display_menu()
        display_menu()
        # ask user: "Enter your choice (1-4): "
        # store input in user_choice
        # convert user_choice to integer
        user_choice = int(input("Enter your choice (1-4): "))

        # if user_choice equals 1
            # if document_path is empty
                # ask user: "Enter the exact file path for your document: "
                # store input in document_path
            # call update_document_info(document_path)

        if user_choice == 1:
            if document_path == "":
                document_path = input("Enter the exact file path for your document: ")
            update_document_info(document_path)

        # elif user_choice equals 2
            # if document_path is empty 
                # ask user for file path
                # store in document_path
            # call view_document(document_path)

        elif user_choice == 2:
            if document_path == "":
                document_path = input("Enter the exact file path for your document: ")
            view_document(document_path)

        # elif user_choice equals 3
            # if document_path is empty
                # ask user for file path
                # store in document_path
            # call add_content_to_document(document_path)

        elif user_choice == 3:
            if document_path == "":
                document_path = input("Enter the exact file path for your document: ")
            add_content_to_document(document_path)

        # elif user_choice equals 4
            # print "Thank you for using the Document Word Count Updater. Goodbye!"
        elif user_choice == 4:
            print("Thank you for using the Document Word Count Updater. Goodbye!")

        # else
            # print "Invalid choice. Please select 1-4."
        else:
            print("Invalid choice. Please select 1-4.")
    # end while loop
    return
# call main() to start program
main()

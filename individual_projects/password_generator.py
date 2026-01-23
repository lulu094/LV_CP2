# LV 1st Random Password Generator
import random
# Main Menu function

#   Display menu options:
#     1. Generate a Password
#     2. Exit
#   Ask user to choose an option - make sure it is a number
#  if choice == 1
#         call generate_password
#   elif choice == 2
#         end program
#         display Goodbye!
#    else
#         print  Please enter a number

def main_menu():
    """Displays the main menu and handles user input"""
    while True:
        print("Main Menu:")
        print("1. Generate a Password")
        print("2. Exit")
        choice = input("Please choose an option (1 or 2): ")
        
        if choice == '1':
            generate_password()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Please enter a valid number (1 or 2).")

# def generate_password():
#     """Generates a random password based on user criteria"""
# make a list for all the lowercase letters, uppercase, numbers, and special characters
# when user tels us the length of the password, make sure it is a number
# The program has to at least generae 4 passwords based on the different combinations of user choices 
# make sure user enter either y/n for the questions
# ask user for password length
# ask user if they want uppercase letters
# ask user if they want numbers
# ask user if they want special characters
# give them 1-4 options based on their choices

def generate_password():
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    special = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length <= 4:
                print("Password length must be at least 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_uppercase = input("Include uppercase letters? (y/n): ").lower()
    use_numbers = input("Include numbers? (y/n):").lower()
    use_special = input("Include special characters? (y/n): ").lower()

    char_pool = lowercase
    if use_uppercase == 'y':
        char_pool += uppercase
    if use_numbers == 'y':
        char_pool += num
    if use_special == 'y':
        char_pool += special

    if len(char_pool) == len(lowercase):
        print("At least one character type must be selected.")
        return

# i need to figure out how to number the 4 passwords generated


# Main loop
main_menu()
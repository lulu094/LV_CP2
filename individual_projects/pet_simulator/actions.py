# LV 1st Actions and menu

# Function feeding_menu(pet):
def feeding_menu(pet):
    # Display food options:
    # 1. Basic
    # 2. Premium
    # 3. Treat
    # 4. Home-cooked
    print("Food options:")
    print("1. Basic")
    print("2. Premium")
    print("3. Treat")
    print("4. Home-cooked")

    # Ask user for choice
    choice = int(input("Enter your choice: "))

    # If choice == 1:
        # Call pet.feed("basic")
    if choice == 1:
        pet.feed("basic")
    # Elif choice == 2:
        # Call pet.feed("premium")
    elif choice == 2:
        pet.feed("premium")

    # Elif choice == 3:
        # Call pet.feed("treat")
    elif choice == 3:
        pet.feed("treat")
    # Elif choice == 4:
        # Call pet.feed("home")
    elif choice == 4
        pet.feed("home")
    # Else:
        # Print "Invalid input"
    else:
        print("Invalid input")

# Function play_with_pet(pet):
    # Call pet.play()
    # Print result message
def play_with_pet(pet):
    pet.play()
    print(f"You played with {pet.name} and increased happiness!")
# Function put_pet_to_sleep(pet):
    # Call pet.sleep()
    # Print result message
def put_pet_to_sleep(pet):
    pet.sleep()
    print(f"{pet.name} is sleeping and regaining health!")

# Function pet_management():
def pet_management():
    # Display pet list
    print("Your pets:")
    for i, pet in enumerate(pets):
        print(f"{i+1}. {pet.name} (Health: {pet.health}, Happiness: {pet.happiness})")
    # Show options:
    # 1. Create new pet
    # 2. Switch pet
    # 3. Delete pet
    print("Options:")
    print("1. Create new pet")
    print("2. Switch pet")
    print("3. Delete pet")
    # Get user input
    choice = int(input("Enter your choice: "))

    # If choice == 1:
        # Call create_pet()
    if choice == 1:
        create_pet()
    # Elif choice == 2:
        # Let user pick pet
        # Set current_pet
    elif choice == 2:
        pet_number = int(input("Enter pet number to switch to: "))
        current_pet = pets[pet_number-1]

    # Elif choice == 3:
        # Remove pet from list
    elif choice == 3:
        pet.pop(int(input("Enter pet number to delete: "))-1)

    # Else:
        # Print invalid input
    else:
        print("Invalid choice")

# Function create_pet():
def create_pet():
    # Ask user for name
    # Ask user for species

    # Create new Pet object
    # Add pet to list

    # Return new pet
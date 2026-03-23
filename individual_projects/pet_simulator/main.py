# LV 1st Main Pet Simulator

# Start program
# Create empty list of pets
# Set current_pet to None
# Set game_running to True
# Set time to Day 1, 08:00
pets = []
current_pet = None
game_running = True
hour = 8
day = 1
# Display welcome message
print("Welcome to the Pet Simulator Game!")
# Call function to create first pet
# Set current_pet to new pet
create_pet()
current_pet = pets[0]

def main():
    # While game_running is True:
    while game_running is True:

        # Display main menu
        # Show current pet info
        # Show current time
        print(f"Current pet: {current_pet.name} (Health: {current_pet.health}, Happiness: {current_pet.happiness})")
        print(f"Time: Day {day}, {hour}:00")
        print("Main Menu:")
        print("1. Feed pet")

        # Ask user for choice

        # If choice == 1:
        # Call feeding_menu(current_pet)
        if choice == 1:
            feeding_menu(current_pet)

        # Else if choice == 2:
        # Call play_with_pet(current_pet)
        elif choice == 2:
            play_with_pet(current_pet)

        # Else if choice == 3:
        # Call put_pet_to_sleep(current_pet)
    
        # Else if choice == 4:
        # Call display_status(current_pet)

        # Else if choice == 5:
        # Call pet_management()

        # Else if choice == 6:
        # Call save_game()

        # Else if choice == 7:
        # Call load_game()

        # Else if choice == 8:
        # Set game_running to False

        # Else:
        # Print "Invalid input"

        # Call advance_time()
        # Call random_event(current_pet)

# End program
# Print goodbye message

#Do pseudocode for extra credit
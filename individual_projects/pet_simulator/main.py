# LV 1st Main Pet Simulator

# Start program
# Create empty list of pets
# Set current_pet to None
# Set game_running to True
# Set time to Day 1, 08:00


    # While game_running is True:
   
        # Display main menu
        # Show current pet info
        # Show current time
        
        # Ask user for choice

        # If choice == 1:
        # Call feeding_menu(current_pet)
       
        # Else if choice == 2:
        # Call play_with_pet(current_pet)
       
        # Elif choice == 3:
        # Call put_pet_to_sleep(current_pet)
       
        # Elif choice == 4:
        # Call display_status(current_pet)
       
        # Elif choice == 5:
        # Call pet_management()
       
        # Elif choice == 6:
        # Call save_game()
  
        # Elif choice == 7:
        # Call load_game()
      
        # Elif choice == 8:
        # Set game_running to False
     
        # Else:
        # Print "Invalid input"
       
        # Call advance_time()
        # Call random_event(current_pet)
      
# End program
# Print goodbye message

#Do pseudocode for extra credit
from actions import create_pet, feeding_menu, play_with_pet, put_pet_to_sleep, pet_management, pet_shop
from game_system import advance_time, random_event, save_game, load_game

def main_game():
    # Local variables
    pets_list, current_pet = [], None
    pets_list, current_pet = create_pet(pets_list)  # Create first pet
    hour, day = 8, 1
    running = True

    while running:
        print(f"\nCurrent pet: {current_pet.name} "
              f"(Health: {current_pet.health}, Happiness: {current_pet.happiness}, Coins: {getattr(current_pet, 'coins', 0)})")
        print(f"Time: Day {day}, {hour}:00")
        print("1. Feed\n2. Play\n3. Sleep\n4. Status\n5. Pet management\n6. Shop\n7. Save\n8. Load\n9. Quit")
        
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            feeding_menu(current_pet)
        elif choice == 2:
            play_with_pet(current_pet)
        elif choice == 3:
            put_pet_to_sleep(current_pet)
        elif choice == 4:
            current_pet.display_status()
        elif choice == 5:
            pets_list, current_pet = pet_management(pets_list, current_pet)
        elif choice == 6:
            pet_shop(current_pet)
        elif choice == 7:
            save_game(pets_list)
            print("Game saved!")
        elif choice == 8:
            pets_list, current_pet = load_game()
            print("Game loaded!")
        elif choice == 9:
            running = False
        else:
            print("Invalid choice.")

        hour, day = advance_time(hour, day)
        random_event(current_pet)

    print("Thanks for playing!")

main_game()
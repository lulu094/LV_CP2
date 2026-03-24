# LV 1st Actions and menu

# Function feeding_menu(pet):
    # Display food options:
    # 1. Basic
    # 2. Premium
    # 3. Treat
    # 4. Home-cooked
   
    # Ask user for choice

    # If choice == 1:
        # Call pet.feed("basic")
   
    # Elif choice == 2:
        # Call pet.feed("premium")
 

    # Elif choice == 3:
        # Call pet.feed("treat")
   
    # Elif choice == 4:
        # Call pet.feed("home")
    
    # Else:
        # Print "Invalid input"
   

# Function play_with_pet(pet):
    # Call pet.play()
    # Print result message

# Function put_pet_to_sleep(pet):
    # Call pet.sleep()
    # Print result message


# Function pet_management():
    # Display pet list
    
    # Show options:
    # 1. Create new pet
    # 2. Switch pet
    # 3. Delete pet
 
    # Get user input

    # If choice == 1:
        # Call create_pet()
   
    # Elif choice == 2:
        # Let user pick pet
        # Set current_pet
  

    # Elif choice == 3:
        # Remove pet from list
    
    # Else:
        # Print invalid input

# Function create_pet():
    # Ask user for name
    # Ask user for species
   

    # Create new Pet object
    # Add pet to list

    # Return new pet
# actions.py
import csv
from pet_class import Pet

# -----------------------
# CREATE PET
# -----------------------
def create_pet(pets_list):
    """Create a new pet and add it to pets_list"""
    name = input("Enter pet name: ")
    species = input("Enter pet species: ")
    new_pet = Pet(name, species)
    # Give default coins for shop
    new_pet.coins = 100
    pets_list.append(new_pet)
    return pets_list, new_pet

# -----------------------
# FEEDING MENU
# -----------------------
def feeding_menu(pet):
    """Feed the pet different types of food"""
    print("\nFood options:")
    print("1. Basic Food (+20 Hunger, +5 Happiness)")
    print("2. Premium Food (+40 Hunger, +15 Happiness)")
    print("3. Treat (+10 Hunger, +10 Happiness)")
    print("4. Home-cooked Meal (+30 Hunger, +20 Happiness)")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        pet.feed("basic")
    elif choice == 2:
        pet.feed("premium")
    elif choice == 3:
        pet.feed("treat")
    elif choice == 4:
        pet.feed("home")
    else:
        print("Invalid input.")

# -----------------------
# PLAY WITH PET
# -----------------------
def play_with_pet(pet):
    """Play with the pet"""
    pet.play()
    print(f"You played with {pet.name}! Happiness increased.")

# -----------------------
# PUT PET TO SLEEP
# -----------------------
def put_pet_to_sleep(pet):
    """Make the pet sleep"""
    pet.sleep()
    print(f"{pet.name} is sleeping and regaining energy and health!")

# -----------------------
# PET MANAGEMENT
# -----------------------
def pet_management(pets_list, current_pet):
    """Manage multiple pets"""
    print("\nYour pets:")
    for i, pet in enumerate(pets_list):
        print(f"{i+1}. {pet.name} (Health: {pet.health}, Happiness: {pet.happiness}, Coins: {getattr(pet,'coins',0)})")
    
    print("Options:")
    print("1. Create new pet")
    print("2. Switch pet")
    print("3. Delete pet")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        pets_list, current_pet = create_pet(pets_list)
    elif choice == 2:
        pet_number = int(input("Enter pet number to switch to: "))
        if 1 <= pet_number <= len(pets_list):
            current_pet = pets_list[pet_number-1]
        else:
            print("Invalid pet number.")
    elif choice == 3:
        pet_number = int(input("Enter pet number to delete: "))
        if 1 <= pet_number <= len(pets_list):
            removed_pet = pets_list.pop(pet_number-1)
            print(f"{removed_pet.name} has been removed.")
            if current_pet == removed_pet and pets_list:
                current_pet = pets_list[0]
            elif not pets_list:
                current_pet = None
        else:
            print("Invalid pet number.")
    else:
        print("Invalid choice.")
    
    return pets_list, current_pet

# -----------------------
# PET SHOP
# -----------------------
def pet_shop(current_pet):
    """Shop to buy items using coins"""
    inventory_file = "individual_projects/pet_simulator/inventory.csv"
    
    shop_items = {
        "Basic Food": 5,
        "Premium Food": 15,
        "Treat": 10,
        "Toy": 20,
        "Home-cooked Meal": 25
    }
    
    print("\nWelcome to the Pet Shop!")
    for i, (item, price) in enumerate(shop_items.items(), start=1):
        print(f"{i}. {item} - {price} coins")
    print(f"Your coins: {getattr(current_pet,'coins',0)}")
    
    choice = int(input("Enter the number of the item to buy (0 to exit): "))
    if choice == 0:
        return
    
    items_list = list(shop_items.keys())
    if 1 <= choice <= len(items_list):
        item_name = items_list[choice-1]
        price = shop_items[item_name]
        coins = getattr(current_pet,'coins',0)
        
        if coins >= price:
            coins -= price
            current_pet.coins = coins
            print(f"You bought {item_name}! Coins left: {coins}")
            
            # Update inventory
            inventory = {}
            try:
                with open(inventory_file, newline="") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        inventory[row[0]] = int(row[1])
            except FileNotFoundError:
                inventory = {}
            
            inventory[item_name] = inventory.get(item_name, 0) + 1
            
            # Write back
            with open(inventory_file, "w", newline="") as f:
                writer = csv.writer(f)
                for name, qty in inventory.items():
                    writer.writerow([name, qty])
        else:
            print("Not enough coins!")
    else:
        print("Invalid choice.")
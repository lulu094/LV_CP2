# LV 1st Game System

# Function advance_time():
from random import random


def advance_time():
    # Increase hour by 1
    hour += 1
    # If hour == 24:
        # Reset hour to 0
        # Increase day by 1
    if hour == 24:
        hour = 0
        day += 1

    
# Function random_event(pet):
def random_event(pet):
    # Generate random number

    # If event happens:
    if random_number < event_chance:
        # Randomly choose:
        # Pet gets sick → decrease health
        # Pet finds toy → increase happiness
        random_event = random.choice(["sick", "toy"])
        if random_event == "sick":
            pet.health -= 20
            print(f"Oh no! {pet.name} got sick and lost health!")
        elif random_event == "toy":
            pet.happiness += 20
            print(f"Yay! {pet.name} found a toy and is happy now!")
        # Print event message


# Function save_game():
def save_game():
    # Open file
    with open("savegame.txt", "w") as f:
        # Write all pet data to file
        for pet in pets:
            f.write(f"{pet.name},{pet.health},{pet.happiness}\n")
        return "Game saved successfully!"
    # Close file

    # Print "Game saved"


# Function load_game():
def load_game():
    # Open file
    with open("savegame.txt", "r") as f:
        # Read pet data
        pet_data = f.readlines()
    
    # Restore pets list
    pets.clear()
    for line in pet_data:
        name, health, happiness = line.strip().split(",")
        pets.append(Pet(name, int(health), int(happiness)))
    return
    # Close file

    # Print "Game loaded"
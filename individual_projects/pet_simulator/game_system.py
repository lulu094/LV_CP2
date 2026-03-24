# LV 1st Game System

# Function advance_time():

    # Increase hour by 1
    # If hour == 24:
        # Reset hour to 0
        # Increase day by 1
   

    
# Function random_event(pet):
    # Generate random number

    # If event happens:
        # Randomly choose:
        # Pet gets sick → decrease health
        # Pet finds toy → increase happiness
        # Print event message


# Function save_game():
        # Write all pet data to file
    # Close file

    # Print "Game saved"


# Function load_game():
    # Open file
        # Read pet data
    
    # Restore pets list
   
    # Close file

    # Print "Game loaded"

from random import random, choice
from pet_class import Pet

def advance_time(hour, day):
    hour += 1
    if hour == 24:
        hour = 0
        day += 1
    return hour, day

def random_event(pet):
    if random() < 0.3:
        event = choice(["sick", "toy", "coins"])
        if event == "sick":
            pet.health -= 20
            print(f"Oh no! {pet.name} got sick!")
        elif event == "toy":
            pet.happiness += 20
            print(f"{pet.name} found a toy!")
        elif event == "coins":
            pet.coins += 10
            print(f"{pet.name} earned 10 coins!")

def save_game(pets_list, filename="savegame.txt"):
    with open(filename, "w") as f:
        for pet in pets_list:
            f.write(f"{pet.name},{pet.species},{pet.age},{pet.hunger},{pet.happiness},{pet.energy},{pet.health},{pet.level},{pet.coins},{pet.genes['color']},{pet.genes['size']}\n")

def load_game(filename="savegame.txt"):
    pets_list = []
    try:
        with open(filename, "r") as f:
            for line in f:
                data = line.strip().split(",")
                name, species = data[0], data[1]
                age, hunger, happiness, energy, health, level, coins = map(int, data[2:9])
                genes = {"color": data[9], "size": data[10]}
                pet = Pet(name, species, age, hunger, happiness, energy, health, level, coins=coins, genes=genes)
                pets_list.append(pet)
    except FileNotFoundError:
        print("No save file found.")
    current_pet = pets_list[0] if pets_list else None
    return pets_list, current_pet
# LV 1st Pet Class 

# Define class Pet

    # Attributes:
    # name
    # species
    # age
    # hunger
    # happiness
    # energy
    # health
    # level
    # skills


    # Constructor method:
        # Set name and species
        # Set age = 0
        # Set hunger = 50
        # Set happiness = 50
        # Set energy = 50
        # Set health = 100
        # Set level = 1
        # Set skills = empty list
    

    # Method feed(food_type):
        # If food_type is basic:
            # Increase hunger
            # Increase happiness a little
        # If food_type is premium:
            # Increase hunger more
            # Increase happiness more
        # Limit values to 100
  
    # Method play():
        # Increase happiness
        # Decrease energy
        # Decrease hunger

    # Method sleep():
        # Increase energy
        # Increase health

    # Method update_health():
        # If hunger or energy is too low:
            # Decrease health
        # Else:
            # Increase health slightly

    # Method display_status():
        # Print all pet stats nicely
import random

class Pet:
    def __init__(self, name, species, age=0, hunger=50, happiness=50, energy=50, health=100, level=1, skills=None, coins=0, genes=None):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.health = health
        self.level = level
        self.skills = skills if skills else []
        self.coins = coins
        self.genes = genes if genes else {"color": random.choice(["red","blue","green"]), "size": random.choice(["small","medium","large"])}

    def feed(self, food_type):
        if food_type == "basic":
            self.hunger += 20
            self.happiness += 5
        elif food_type == "premium":
            self.hunger += 40
            self.happiness += 15
        elif food_type == "treat":
            self.hunger += 10
            self.happiness += 10
        elif food_type == "home":
            self.hunger += 30
            self.happiness += 20
        self.hunger = min(self.hunger, 100)
        self.happiness = min(self.happiness, 100)

    def play(self):
        self.happiness += 20
        self.energy -= 10
        self.hunger -= 5
        self.energy = max(min(self.energy, 100), 0)
        self.hunger = max(min(self.hunger, 100), 0)
        self.happiness = min(self.happiness, 100)

    def sleep(self):
        self.energy += 30
        self.health += 10
        self.energy = min(self.energy, 100)
        self.health = min(self.health, 100)

    def update_health(self):
        if self.hunger < 20 or self.energy < 20:
            self.health -= 10
        else:
            self.health += 5
        self.health = max(min(self.health, 100), 0)

    def display_status(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")
        print(f"Health: {self.health}")
        print(f"Level: {self.level}")
        print(f"Skills: {', '.join(self.skills) if self.skills else 'None'}")
        print(f"Coins: {self.coins}")
        print(f"Genes: {self.genes}")

    def breed(self, other_pet):
        child_name = input("Enter name for the new pet: ")
        child_species = self.species if self.species == other_pet.species else input("Enter species for the new pet: ")
        child_genes = {
            "color": random.choice([self.genes["color"], other_pet.genes["color"]]),
            "size": random.choice([self.genes["size"], other_pet.genes["size"]])
        }
        return Pet(child_name, child_species, genes=child_genes)
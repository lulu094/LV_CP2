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
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.age = 0
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.health = 100
        self.level = 1
        self.skills = []
    def __str__(self):
        return f"Name : {self.name}\nSpecies : {self.species}\nAge : {self.age}\nHunger : {self.hunger}\nHappiness : {self.happiness}\nEnergy : {self.energy}\nHealth : {self.health}\nLevel : {self.level}\nSkills : {', '.join(self.skills)}"
    


    # Constructor method:
        # Set name and species
        # Set age = 0
        # Set hunger = 50
        # Set happiness = 50
        # Set energy = 50
        # Set health = 100
        # Set level = 1
        # Set skills = empty list
class method :
    def __init__(self, name, species):  
        self.name = name
        self.species = species
        self.age = 0
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.health = 100
        self.level = 1
        self.skills = []
    

    # Method feed(food_type):
        # If food_type is basic:
            # Increase hunger
            # Increase happiness a little
        # If food_type is premium:
            # Increase hunger more
            # Increase happiness more
        # Limit values to 100
    mehod feed(self, food_type)
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
        
        # Limit values to 100
        if self.hunger > 100:
            self.hunger = 100
        if self.happiness > 100:
            self.happiness = 100

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
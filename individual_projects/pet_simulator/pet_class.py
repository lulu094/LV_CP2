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
# LV 1st Classes Notes

# example 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        
    def __str__(self):
       return f"Name : {self.name}\nSpecies : {self.species} \nAge : {self.age}"
    
    def birthday(self):
        self.age += 1
dog = Animal("Doug", "dog", 4)
bunny = Animal("Judy","rabbit", 2)
print(dog)
print
dog.birthday()
print(dog)

# example 2
class ClassPeriod:
    def _init_(self, subject, teacher = "Mrs. LaRose", room = None):
       self.subject = subject.title()
       self.teacher = teacher
       self.room = room
    
    def __str__(self):
        return f"Subject : {self.subject}\nTeacher : {self.teacher}\nRoom : {self.room}\n"
    

first = ClassPeriod("Computer Programming 2", 200)
second = ClassPeriod("Math","Mrs. Gant",201)
print(first, second)
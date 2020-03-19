class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


my_dog = Dog('Lab', 'Ariel')

other_dog = Dog('Huskee', 'Zebra')
print(my_dog.species)

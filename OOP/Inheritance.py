# INHERITANCE


class Animal():
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        # Animal.__init__(self)
        print('Dog Created')

    def bark(self):
        print('Woof')
    
    def eat(self):
        print("Dog Eating")


my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()

# SPECIAL METHODS

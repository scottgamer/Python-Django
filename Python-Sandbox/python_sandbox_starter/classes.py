# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class


class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

# Extend class


class Customer(User):
  # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Init user obj
richard = User('Richard Munoz', 'rmunoz@tests.com', 27)

# Init customer obj
janet = Customer('Janet', 'janet@test.com', 26, )

# print(type(richard))
# print(richard.name)
print(richard.greeting())

janet.setBalance(500)

print(janet.greeting())

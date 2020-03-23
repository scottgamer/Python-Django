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


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Book destroyed")


book = Book("Python", "Richard", 200)
print(book)
print(len(book))
del book

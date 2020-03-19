class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, radius):
      self.radius = radius


my_circle = Circle(3)
my_circle.set_radius(1000)
print(my_circle.area())

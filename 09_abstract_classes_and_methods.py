# Assignment 09:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().



from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete class that inherits and implements area()
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create a rectangle and get area
r = Rectangle(5, 3)
print("Area:", r.area())  # Output: Area: 15

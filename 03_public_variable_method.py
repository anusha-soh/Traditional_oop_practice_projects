# Assignment 03:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} has started ...")

car = car("Toyota")
print(car.brand)
car.start()


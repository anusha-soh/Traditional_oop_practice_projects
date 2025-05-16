# Assignment 02:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Count: {cls.count}")

Counter()
Counter()
Counter()
Counter()
count = Counter()
count.show_count()
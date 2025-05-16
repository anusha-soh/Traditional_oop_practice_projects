# Assignment06:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Objact has been instanciated... 😊")

    def __del__(self):
        print("Objact has been destroyed... 😵")

log = Logger()

del log
# del Logger
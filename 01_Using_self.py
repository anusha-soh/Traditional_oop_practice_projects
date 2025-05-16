#Assingment 01:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self , name , marks):
        print("Creating instance...")
        self.name = name
        self.marks = marks

    def display(self):
        print(f'name : {self.name}')
        print(f'marks : {self.marks}')

    
student = Student("Ali" , "90")
student.display()
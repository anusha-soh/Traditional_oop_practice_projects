# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# Employee class (independent)
class Employee:
    def __init__(self, name):
        self.name = name

# Department class (stores reference to Employee)
class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee
    def show_details(self):
        print(f"Department: {self.name}, Employee: {self.employee.name}")

# Create an employee (independent object)
emp = Employee("Ali")

# Create a department and link the employee
dept = Department("HR", emp)

# Show the details
dept.show_details()  

print(emp.name) 
# Assignment 07:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self,):
        self.name = 'Hasan'
        self._salary = 10000
        self.__ssn = "230RT"
    
emp = Employee()
print(emp._salary)


# print(emp.__ssn)   #Error


print(emp._Employee__ssn)  # Valid code ✅
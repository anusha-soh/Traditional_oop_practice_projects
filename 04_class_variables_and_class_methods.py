# Assignment 04:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "HBL"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

bank = Bank()
print(Bank.bank_name)
bank.change_bank_name("Al Habib")
print(Bank.bank_name)
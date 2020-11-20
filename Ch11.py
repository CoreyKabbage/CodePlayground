from city_functions import test_city_country

exercise = int(input("Which exercise?\n"))

class Employee():
    def __init__(self, first_name, last_name, salary, raise_amount):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.raise_amount = 5000
    
    def set_raise_amount(self, raise_amount):
        self.raise_amount = raise_amount

def test_give_default_raise(self, salary, raise_amount):
        if raise_amount == 5000:
            self.salary += raise_amount
            print(f"You got a raise of {self.raise_amount}, you now make {self.salary}")
        else:
            print("That's not the default raise amount.")

def test_give_custom_raise(self, salary, raise_amount):
        if raise_amount != 5000:
            self.salary += raise_amount
            print(f"You got a raise of {self.raise_amount}, you now make {self.salary}")
        else:
            print("That's the default raise amount!")

if exercise == 1:
    test_city_country("santiago", "chile")
if exercise == 2:
    test_city_country("santiago", "chile", 5000000)
if exercise == 3:
    test_employee = Employee("Corey", "Kabbage", salary=10000, raise_amount=5000)
    test_give_default_raise(test_employee, test_employee.salary, test_employee.raise_amount)
    test_employee.raise_amount = 10000
    test_give_custom_raise(test_employee, test_employee.salary, test_employee.raise_amount)    
else:
    pass
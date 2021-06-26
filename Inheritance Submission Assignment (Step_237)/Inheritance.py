# Python Course - Step 237 ("Inheritance Submission Assingment")
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4

# 'Business' is the parent class, created with 5 inheritable attributes:
'''
class Business:
    name = input("What is your business's name?")
    location = input("What is your business's address?")
    phone = input("What is your business's phone number?")
    industry = input("What industry does your business operate within?")
    employees = input("How many employees work at your business?")


# 'DayCareCenter' is the 1st child class; it inherits all 5 of the 'Business' \
# class's attributes, but adds three attributes of its own:
class DayCareCenter(Business):
    certified = True
    clients = 20
    afterHours = False

# 'utilityCompany' is the 2nd child class; also inheriting all 5 of the 'Business'\
# class's attributes, while having four of its own attributes:
class utilityCompany(Business):
    maxOutput = "400,000 MWh"
    serviceArea = "Southwest"
    EnviroImpactIndex = 23
    lobbyists = True
'''
#----------------------------------------------
#   Objectives of Step 241:
#       a) Create a class,
#       b) Create an object,
#       c) Assign values to the object props using __init__, and...
#       d) Create a method in the class

class Vehicle: # (Part a)
    def __init__(self, name, operable, VIN, tires, insured, propulsion): # (Part c)
        self.name = name
        self.operable = operable
        self.VIN = VIN
        self.tires = tires
        self.insured = insured
        self.propulsion = propulsion

    def movement(self): # (Part d)
        print('Every {} is propelled via {}'.format(self.name, self.propulsion))

bicycle = Vehicle("Schwinn", True, "1000001", True, False, "peddling") # (Part b)
'''
print('This vehicle OBJECT is a {}; is it operable, True or False?: {}'.format(bicycle.name, bicycle.operable))
print("This vehicle's VIN is {}; does it have tires, True or False?: {}".format(bicycle.VIN, bicycle.tires))
print('This vehicle is insured, True or False?: {}'.format(bicycle.insured))
print(bicycle.movement())
'''

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print('For this 2nd class, My name is {} {}\nstop'.format(self.firstName, self.lastName))

myself = Person("Douglas", "Foreman")

if __name__ == "__main__":
    print(myself.printName())

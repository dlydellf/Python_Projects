# Python Course - Step 278 ("Encapsulation Submission Assignment")
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4
#---------------------------------------
#   Objectives of Step 278:
#       a) Create a CLASS that uses encapsulation,
#       b) Class should make use of a PRIVATE attribute or function,
#       c) Class should make use of a PROTECTED attribute or function, and
#       d) Create an OBJECT that makes use of protected & private
#---------------------------------------


# The Parent class:
class Vehicle: # (Part a) Creating a class that uses ENCAPSULATION
    def __init__(self):
        self.__privateVIN = 123456789 # (Part b) Class making use of a PRIVATE attribute
        self._protectedVIN = 987654321 # (Part c) Class makes use of a PROTECTED attribute

    def printPrivateVIN(self): # (Part b) Class making use of a PRIVATE function
        print(self.__privateVIN)

    def printProtectedVIN(self): # (Part c) Class makes use of a PROTECTED function
        print(self._protectedVIN)

# The created OBJECT:
newCar = Vehicle() # (Part d) Here, an OBJECT is being created

# Object uses Class's PRIVATE & PROTECTED attributes & functions:
newCar.printPrivateVIN() # (Part d) Object's usage of PRIVATE
newCar.printProtectedVIN() # (Part d) Object's usage of PROTECTED

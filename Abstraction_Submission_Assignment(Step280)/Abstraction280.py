# Python Course - Step 280 ("Abstraction Submission Assignment")
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4
#---------------------------------------
#   Objectives of Step 280:
#       a) Create a PARENT CLASS that uses abstraction,
#       b) Parent class should contain one ABSTRACT method & one REGULAR method,
#       c) Create a CHILD CLASS that defines the implementation of its parent's abstract method,
#       d) Create an OBJECT that utilizes both the parent & child methods.
#---------------------------------------


# Importing 'abstractmethod' from the abc (Abstract Base Class) module:
from abc import ABC, abstractmethod

#(Part a) The PARENT CLASS that will use abstraction:
class Vehicle(ABC):
    #(Part b) The ABSTRACT method:
    @abstractmethod
    def printAbstractData(self, *arg): #This function allows passing in (an) argument(s) without knowing how or what kind of data it(they) will be
        pass
    
    #(Part b) The REGULAR method:
    def printVIN(self, VIN):
        print('The VIN of this vehicle is {}.'.format(VIN))
    
#(Part c) The CHILD CLASS, defining its parent's abstract method:
class Car(Vehicle):
    def printAbstractData(self, *arg):
        print('The {} of this new car is {}.'.format(*arg))

#(Part d) The created OBJECT:
newCar = Car()
newCar.printVIN(135792468) # (Part d) Object's usage of PARENT's method
newCar.printAbstractData('VIN', '13579') # (Part d) Object's usage of CHILD's method

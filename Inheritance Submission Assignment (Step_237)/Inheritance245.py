# Python Course - Step 245 ("Polymorphism Submission Assignment")
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4
#---------------------------------------
#   Objectives of Step 245:
#       a) Create two classes that inherit from another class,
#       b) Each child has two or more of their own attributes,
#       c) Parent class has at least one method, and
#       d) Both children use polymorphism on the parent class
#---------------------------------------


# The Parent class:
class Vehicle:
    def __init__(self, name, propulsion, tires, VIN, operable, insured):
         self.name = name
         self.propulsion = propulsion
         self.tires = tires
         self.VIN = VIN
         self.operable = operable
         self.insured = insured

    def movement(self): # (Part c)
        print('(T/F) Does this vehicle have tires?: {}\nRegardless, this {} moves via {}' \
              .format(self.tires, self.name, self.propulsion.upper()))

    def identification(self): # (Part c)
        if self.operable:
            print('Since this {} IS operable, it MUST maintain "{}" insurance \ncoverage at'\
                  ' all times, with insurance registered under the VIN: {}'.format(self.name, \
                                                                                  self.insured, self.VIN))
        else:
            print('Since this {} is NOT operable, its VIN ({}) is allowed an insurance status'\
                  ' of: "{}"'.format(self.name, self.VIN, self.operable))

'''
#Tested both Vehicle methods & all three outputs - gtg
testCar = Vehicle("car", "gas engine", True, 1234567890, False, True)
print(testCar.movement())
print(testCar.identification())
'''
            
# 1st Child class:
class Bicycle(Vehicle): # (Part a)
    def __init__(self, name, propulsion, tires, VIN, operable, insured, lifecycle, gender, brand, color): # (Part b)
        super().__init__(name, propulsion, tires, VIN, operable, insured) # (Part a)
        self.lifecycle = lifecycle
        self.gender = gender
        self.brand = brand
        self.color = color

    def movement(self): # (Part d)
        print('Since this {} {} has tires, it moves via {}'.format(self.brand, self.name, self.propulsion))

    def identification(self): # (Part d)
        if self.insured:
            print('This {} {} {}, designed for {} {} riders, is insured under its VIN: ({}'\
                  ')'.format(self.color, self.brand, self.name, self.lifecycle, self.gender, self.VIN))
        else:
            print('This {} {} {} with a VIN of ({}) has no listed insurance coverage'.format\
                  (self.color, self.brand, self.gender, self.VIN))

'''
#Tested both Bicycle methods & their three outputs - gtg
bike = Bicycle("bicycle", "pedals", True, 987654321, True, True, "Adult", "male", "Schwinn", "red")
print(bike.movement())  
print(bike.identification())
'''


# 2nd Child class:
class Airplane(Vehicle): # (Part a)
    def __init__(self, name, propulsion, tires, VIN, operable, insured, registration, Range, \
                 groundSpeed, airspeed, length, wingspan, height, operatingNoiseLevel): # (Part b)
        super().__init__(name, propulsion, tires, VIN, operable, insured) # (Part a)
        self.registration = registration
        self.Range = Range        
        self.groundSpeed = groundSpeed
        self.airspeed = airspeed
        self.length = length
        self.wingspan = wingspan
        self.height = height
        self.operatingNoiseLevel = operatingNoiseLevel

    def movement(self): # (Part d)
        print('The aircraft with identifier {} has submitted a flight plan well within its operating '\
              'range of {} miles; local winds should increase its {} airspeed to a ground speed of ap'\
              'proximately {}'.format(self.registration, self.Range, self.airspeed, self.groundSpeed))
        
    def identification(self): # (Part d)
        print('For Aircraft {}:\n\tLength: {}\n\tWingspan: {}\n\tHeight: {}\n\tOperating Noise Level (dB): {}'. \
                  format(self.registration.upper(), self.length, self.wingspan, self.height, self.operatingNoiseLevel))
'''
#Tested both Airplane methods & their outputs - gtg
plane = Airplane("Boeing 747-8", "four General Electric GEnx-2B67", True, "28000 / 29000", True, True, "Air Force One", "unlimited", \
         '"Classified"', '"Classified"', "250 ft' 2\"", "224' 5\"", "63' 6\"", '"Classified"')
print(plane.movement())
print(plane.identification())
'''

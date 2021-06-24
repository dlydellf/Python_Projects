# Python Course - Step 237 ("Inheritance Submission Assingment")
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4

# 'Business' is the parent class, created with 5 inheritable attributes:
class Business:
    name = "What is your business's name?"
    location = "What is your business's address?"
    phone = "What is your business's phone number?"
    industry = "What industry does your business operate within?"
    employees = "How many employees work at your business?"


# 'DayCareCenter' is the 1st child class; it inherits all 5 of the 'Business' \
# class's attributes, but adds three attributes of its own:
class DayCareCenter(Business):
    certified = True
    clients = 20
    afterHours = False

# 'utilityCompany' is the 2nd child class; also inheriting all 5 of the 'Business'\
# class's attributes, while having four of its own attributes:
class utilityCompany(Business):
    maxOutput = 400,000 MWh
    serviceArea = "Southwest"
    EnviroImpactIndex = 23
    lobbyists = True
        

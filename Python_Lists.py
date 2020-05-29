# Python  Lists 

#________1. Create a list -
'''As opposed to int, bool etc., a list is a compound data type; you can group values together:'''

a = "is"
b = "nice"
my_list = ["my", "list", a, b]
print(my_list)

# Ex. 1:
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# Ex. 2:
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall,"kitchen", kit, "living room", liv,"bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

#________2.List of lists - A list can contain any Python type. But a list itself is also a Python type. That means that a list can also contain a list! Python is getting funkier by the minute, but fear not, just remember the list syntax:

# my_list = [el1, el2, el3]

# Ex. 1:
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)


# Print out the type of house
print(type(house))



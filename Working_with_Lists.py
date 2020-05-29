#________Replace list elements -
x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]

# Ex. 1:
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[9] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

#________Extend a list -
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]

# Ex. 1:
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage" , 15.45]

#________Delete list elements -
x = ["a", "b", "c", "d"]
del(x[1])

#________Inner workings of lists -
'''If you want to prevent changes in areas_copy from also taking effect in areas, you'll have to do a more explicit copy of the areas list. You can do this with list() or by using [:].'''

# Ex. 1:
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
#!/bin/python3

# Creating a list called subjects

subjects = ["physics", "calculus", "poetry", "history"]


# Creating a list called grades

grades = [98, 97, 85, 88]

# Creating a two-dimensional list to combine subjects and grades

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]


print(gradebook)


gradebook.append(["computer science", 100])


gradebook.append(["visual arts", 93])



# Modifying the grade for "visual arts" by accessing the index and adding 5

gradebook[4][1] += 5



# Removing the grade value for poetry using the .remove() method

gradebook.remove(["poetry", 85])



# Adding a new "Pass" value

gradebook.insert(2, ["poetry", "Pass"])



# Combining last_semester_gradebook and gradebook into full_gradebook

last_semester_gradebook = [["Biology", 87], ["History", 92], ["Psychology", 91]]

full_gradebook = last_semester_gradebook + gradebook



# Printing full_gradebook

print(full_gradebook)

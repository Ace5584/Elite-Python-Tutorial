# Section 6 Module 3 Part 1
# [Class Roll]
#############################################################################
# Task Description:
#   A class role will be entered with a space separating each name.
#   Then you want to print out a sorted role with the title of Class Roll.
#   Example is show below
#############################################################################
# Your Output should be like this:
# Students: Peng Ivan Alan Jodi Macy
# Class Roll
# Alan
# Ivan
# Jodi
# Macy
# Peng
#############################################################################

data = input("Students: ")
students = data.split(" ")
students.sort()
print("Class Roll")
for student in students:
    print(student)


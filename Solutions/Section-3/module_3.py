# Section 3 Module 3
# [You're Broke!]
#############################################################################
# Task Description:
#   You have to write a program that prints "You're Broke :(" if the user
#   enters zero or less, and print "You're fine :)" if the user enters
#   a positive number
#############################################################################
# Your Output should be like this:
# Number: 69
# You're fine :)

# Number: -2
# You're broke :(
#############################################################################

# num = float(input("Number: "))
# if num > 0:
#     print("you're fine :)")
# else:
#     print("You're broke :(")

num = float(input("Number: "))
if num <= 0:
    print("You're broke :(")
else:
    print("you're fine :)")


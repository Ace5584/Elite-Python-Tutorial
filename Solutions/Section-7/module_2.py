# Section 7 Module 2
# [Guessing Game]
#############################################################################
# Task Description:
#   Create a program that asks for input on what the robot's favourite food
#   is. Continue looping through it until the user enters the correct answer.
#   An Example will be shown below.
#############################################################################
# Your Output should be like this:
# What is my favourite food?
# Guess? chips
# Not even close.
# Guess? broccoli
# Not even close.
# Guess? electricity
# You guessed it! Buzzzz
#############################################################################

# Solution Number 1:
# print("What is my favourite food? ")
# answer = input("Guess? ")
# while answer:
#     if answer == "electricity":
#         print("You guessed it! Buzzzz")
#         break
#     else:
#         print("Not even close. ")
#     answer = input("Guess? ")

print("What is my favourite food? ")
answer = input("Guess? ")
while answer != "electricity":
    print("Not even close. ")
    answer = input("Guess? ")
print("You guessed it! Buzzzz")


# Section 2 Module 3
# [Annoying Bot]
#############################################################################
# Task Description:
#   You have to write a program that repeat something you say the amount of
#   times you want it to repeat for.
#############################################################################
# Your Output should be like this:
# What do you want me to say? spam
# How many times do you want me to say it? 5
# spamspamspamspamspam
#############################################################################

userString = input("What do you want me to say? ")
userNum = int(input("How many times do you want me to say it? "))
output = userString * userNum

print(output)


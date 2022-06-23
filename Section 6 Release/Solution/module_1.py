# Section 6 module 1
# [Python Calculator]
#############################################################################
# Task Description:
# Create a simple python calculator that takes two input that are numbers and
# then have a second input that decides whether to multiply the first number
# by the second number or to divide the first number by the second number
#############################################################################
# Your Output should be like this:
# First Number: 2
# Second Number: 2
# Operation: *
# 4

# First Number: 2
# Second Number: 2
# Operation: /
# 1.0
#############################################################################

firstNum = float(input("First Number: "))
SecondNum = float(input("Second Number: "))
operator = input("Operation: ")

if operator == "/":
    print(firstNum / SecondNum)
elif operator == "*":
    print(firstNum * SecondNum)
else:
    print("Please enter a valid operator (/ or *)")

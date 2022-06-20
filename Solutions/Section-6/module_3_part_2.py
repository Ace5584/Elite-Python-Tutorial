# Section 6 Module 3 Part 2
# [Spending Total]
#############################################################################
# Task Description:
#   A group of numbers will be entered with a space separating. Then you
#   need to combine each number and print out a total
#############################################################################
# Your Output should be like this:
# Enter the expenses: 10 2 5 15
# Total: $32

# Enter the expenses: 1 2 3 4 5 100
# Total: $115
#############################################################################

data = input("Enter the expenses: ")
expenses = data.split(" ")
total = 0
for expense in expenses:
    total = total + int(expense)
print("Total: $" + str(total))


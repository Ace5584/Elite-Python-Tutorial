# Section 5 Module 2
# [Just Count]
#############################################################################
# Task Description:
#   Write a program that counts to the number the user enters
#############################################################################
# Your Output should be like this:
# Enter a number: 7
# 1
# 2
# 3
# 4
# 5
# 6
# 7
#############################################################################

num = int(input("Enter a number: "))
for i in range(1, num+1):
    print(i)

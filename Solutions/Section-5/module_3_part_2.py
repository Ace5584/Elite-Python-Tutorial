# Section 5 Module 3 Part 2
# [printing backwards]
#############################################################################
# Task Description:
#   You have to write a program that inputs a sentence and then print out the
#   statement backwards. Example shown below
#############################################################################
# Your Output should be like this:
# Line: This is an example line of text.
# .txet fo enil elpmaxe na si sihT

# Line: HeLLo ThErE!
# !ErEhT oLLeH
#############################################################################

msg = input("Line: ")
reversed = ""
for i in range(len(msg)-1, -1, -1):
    reversed = reversed + msg[i]
print(reversed)


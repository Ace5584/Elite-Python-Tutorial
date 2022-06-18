# Section 4 Module 3 Part 1
# [Broken Keyboard]
#############################################################################
# Task Description:
#   Your friend Dave's keyboard is broken, his "a", "e", and "o" keys are
#   broken. When he types o, he types ###, when he types e, he types ##.
#   And when he types a, he types %% instead.
#############################################################################
# Your Output should be like this:
# What did he say? My k##ybo%%rd is br###k##n :(
# he meant to say: My keyboard is broken :(
#############################################################################

statement = input("What did he say? ")
statement = statement.replace('###', "o")
statement = statement.replace('##', "e")
statement = statement.replace('%%', "a")
print(statement)


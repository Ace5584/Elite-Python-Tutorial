# Section 7 Module 3 Part 2
# [Going up the lift]
#############################################################################
# Task Description:
#   Create an elevator program that allows the user to enter a current floor
#   and the destination floor and then print out the levels to get to the
#   destination level. Example shown below
#############################################################################
# Your Output should be like this:
# Current floor: 3
# Destination floor: 6
# Level 3
# Level 4
# Level 5
# Level 6

# Current floor: 1
# Destination floor: 2
# Level 1
# Level 2
#############################################################################

current = int(input("Current floor: "))
destination = int(input("Destination floor: "))
difference = current - destination
# If difference is a positive value EG:
#   2 - 1 = 1
#   down
# If difference is a negative value EG:
#   1 - 2 = -1
#   up
if difference > 0:
    while destination <= current:
        print("Level ", current)
        current -= 1
elif difference < 0:
    while destination >= current:
        print("Level ", current)
        current += 1


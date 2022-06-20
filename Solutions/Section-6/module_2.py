# Section 6 Module 2
# [Weather Report]
#############################################################################
# Task Description:
#   Write a program that reads a sentence of days and then count the amount
#   of days it rains. Each day is separated with a space. Example shown below
#############################################################################
# Your Output should be like this:
# Which days was raining? Monday Tuesday Wednesday
# Number of days without rain: 4

# Which days was raining? Thurs
# Number of days without rain: 6
#############################################################################

days = input("Which days was raining? ")
lsDays = days.split(" ")
noRain = 7 - len(lsDays)
print("Number of days without rain:", noRain)



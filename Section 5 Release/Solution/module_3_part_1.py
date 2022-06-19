# Section 5 Module 3 Part 1
# [Secret Agent]
#############################################################################
# Task Description:
#   Write a code that takes the third character of a string and put them
#   together to piece out a secret message. Example shown below.
#############################################################################
# Your Output should be like this:
# Message? cxohawalkldflghemwnsegfaeap
# c h a l l e n g e

# Message? pbaynatnahproarnsm
# p y t h o n
#############################################################################

msg = input("Message? ")
decoded = ""
for i in range(0, len(msg), 3):
    decoded = decoded + msg[i] + " "

decoded = decoded.rstrip()
print(decoded)

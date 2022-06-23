# Section 8 Module 3 Part 1
# [Robot coms]
#############################################################################
# Task Description:
#   The robots' coms are encoded. To decode the message:
#       - They read the words in reverse order
#       - They only pay attention to the words that start with an uppercase
#   An example of this is shown below
#############################################################################
# Your Output should be like this:
# code: BaSe fOO ThE AttAcK
# decoded: attack the base

# code: soMe SuPPLies liKE Ice-cREAm aRe iMPORtant oNly tO THeir cReaTORS. tO
# DestroY thEm iS pOInTLess.
# decoded: destroy their ice-cream supplies
#############################################################################

code = input("code: ")

lsCode = code.split(" ")
lsCode = lsCode[::-1]
final = []

for i in lsCode:
    if i[0].isupper():
        final.append(i.lower())

print(" ".join(final))




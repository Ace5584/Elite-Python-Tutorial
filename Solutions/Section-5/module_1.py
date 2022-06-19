# Section 5 module 1
# [Give me a G!]
#############################################################################
# Task Description:
# You will write a program that loops through the chant that the user inputs
# and then add "Give me a " to the front of each letter that is being looped
# and repeat the letter after that again with a "!". Then, after you loop
# through the entire thing, print "What does it spell? Then repeat the word
# in all caps. Example shown below
#############################################################################
# Your Output should be like this:
# Cheer: gryffindor
# Give me a g, g!
# Give me a r, r!
# Give me a y, y!
# Give me a f, f!
# Give me a f, f!
# Give me a i, i!
# Give me a n, n!
# Give me a d, d!
# Give me a o, o!
# Give me a r, r!
# What does it spell?
# GRYFFINDOR

# Cheer: hello
# Give me a h, h!
# Give me a e, e!
# Give me a l, l!
# Give me a l, l!
# Give me a o, o!
# What does it spell?
# HELLO
#############################################################################

chant = input("Cheer: ")

for i in chant:
    print("Give me a " + i + ", " + i + "!")
print("What does it spell? ")
print(chant.upper())



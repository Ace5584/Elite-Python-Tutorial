# Section 8 Module 3 Part 2
# [Super Anagram]
#############################################################################
# Task Description:
#   A super anagram are two words that contains the same set of letters and
#   the first and last letters are the same. Write a program that detects
#   super anagram. If it is a super anagram, print out "Super Anagram!" and
#   print "Huh?" if it isn't
#############################################################################
# Your Output should be like this:
# Enter words: brain brian
# Super Anagram!

# Enter words: too two
# Huh?
#############################################################################

data = input("Enter words: ")
word1 = data.split(" ")[0]
word2 = data.split(" ")[1]

lsWord1 = list(word1)
lsWord2 = list(word2)
lsWord1.sort()
lsWord2.sort()

if lsWord1 == lsWord2:
    if word1[0] == word2[0] and word1[len(word1)-1] == word2[len(word2)-1]:
        print("Super Anagram!")
else:
    print("Huh?")




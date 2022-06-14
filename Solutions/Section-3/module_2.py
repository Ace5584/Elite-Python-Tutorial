# Section 3 Module 2
# [Access Denied]
#############################################################################
# Task Description:
#   You have to write a program that prints Access Granted if you enter the
#   correct password and print Access Denied if the password is incorrect.
#   The password is: Ab32kss92l
#############################################################################
# Your Output should be like this:
# Enter password: Ab32kss92l
# Access granted

# Enter password: Hello
# Access denied
#############################################################################

password = input("Enter Password: ")
if password == "Ab32kss92l":
    print("Access granted")
else:
    print("Access denied")



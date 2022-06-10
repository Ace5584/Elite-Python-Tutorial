# This program converts Celsius to Fahrenheit

s = input("Enter the temperature in degree Celsius: ")
c = int(s)
f = c*9/5 + 32
print("The temperature is", f, "degree Fahrenheit")

s2 = input("Enter the temperature in degree Fahrenheit: ")
f2 = int(s2)
c2 = (32 * f2 - 32) * 5/9
print("The temperature is", c2, "degree Celsius")


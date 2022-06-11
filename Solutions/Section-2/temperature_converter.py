# Temperature Converter
# The program will convert Celsius to Fahrenheit according to what the user enters
# The program will then take another input that will convert Fahrenheit to Celsius

firstTemp = int(input("Enter a temperature to convert from Celsius to Fahrenheit: "))
firstResult = (firstTemp * 9//5) + 32
print(firstResult, "degrees Fahrenheit")

secondTemp = int(input("Enter a temperature to convert from Fahrenheit to Celsius: "))
secondResult = (secondTemp - 32) * 5//9
print(secondResult, "degrees Celsius")


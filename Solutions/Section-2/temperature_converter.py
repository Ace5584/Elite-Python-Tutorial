# This program will convert user's inputted temperature in celsius to fahrenheit
# And then after that, this program will require another input from the user that will convert
# the inputted temperature in fahrenheit to celsius

inputTemp_1 = int(input("Enter the temperature in degree Celsius: "))
tempC_1 = inputTemp_1
tempF_1 = (tempC_1 * 9/5) + 32
print("The temperature is", tempF_1, "degree Fahrenheit")

inputTemp_2 = int(input("Enter the temperature in degree Fahrenheit: "))
tempF_2 = inputTemp_2
tempC_2 = (tempF_2 - 32) * 5/9
print("The temperature is", tempC_2, "degree Celsius")


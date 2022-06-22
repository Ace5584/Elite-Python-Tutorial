# Choose the first number to test, start with 1
# See if that number divides evenly into 540 using the modulus operator, if it does print it out as a factor;
# Choose the next number by adding 1 to your last choice;
# If your number to test is greater than 540 then you have finished, otherwise go back to step 2.

num = 1
while num <= 540:
    if (540 % num) == 0:
        print(num)
    num += 1
    # num = num + 1


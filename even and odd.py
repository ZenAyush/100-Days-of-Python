num = int(input("Which number do you want to check? "))  # prompts the user to enter a number and stores it in the variable 'num'

if num % 2 == 0:  # checks if the number is divisible by 2 using the modulo operator
    print("It is a Even Number.")  # prints "It is a Even Number." if the number is even
else:
    print("It is a Odd Number.")  # prints "It is a Odd Number." if the number is odd
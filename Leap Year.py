# Prompt the user to enter a year to be checked
year = int(input("Which year do you want to check? "))

# Check if the year is divisible by 4
if year % 4 == 0:
    # If the year is divisible by 4, check if it is divisible by 100
    if year % 100 == 0:
        # If the year is divisible by 100, check if it is divisible by 400
        if year % 400 == 0:
            # If the year is divisible by 400, it is a leap year
            print("It is a Leap Year.")
        else:
            # If the year is not divisible by 400, it is not a leap year
            print("It is not a Leap Year.")
    else:
        # If the year is not divisible by 100, but is divisible by 4, it is a leap year
        print("It is a Leap Year.")
else:
    # If the year is not divisible by 4, it is not a leap year
    print("It is not a Leap Year.")
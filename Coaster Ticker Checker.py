# This program checks if a person's height is greater than 120 cm to determine if they can ride a rollercoaster.

# Print a welcome message to the user
print("Welcome to the rollercoaster!")

# Prompt the user to enter their height in centimeters and store the value as an integer in the variable 'height'
height = int(input("What is your height in cm? "))

# Check if the height is greater than 120 cm using an if statement
if height > 120:
    # If the height is greater than 120 cm, print a message saying the user can ride the rollercoaster
    print("You can ride the rollercoaster!")
else:
    # If the height is less than or equal to 120 cm, print a message saying the user can't ride the rollercoaster
    print("Sorry, You can't ride the rollercoaster!")
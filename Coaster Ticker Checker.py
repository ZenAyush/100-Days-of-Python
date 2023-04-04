# This program checks if a person's height is greater than 120 cm to determine if they can ride a rollercoaster.

# Print a welcome message to the user
print("Welcome to the rollercoaster!")

# Prompt the user to enter their height in centimeters and store the value as an integer in the variable 'height'
height = int(input("What is your height in cm? "))
bill = 0

# Check if the user's height is greater than or equal to 120 cm
if height >= 120:

    # Prompt the user to enter their age
    age = int(input("What is your age? "))
    # Calculate the appropriate fee based on the user's age
    if age < 12:
        bill = 5
        print("Child ticktes are 5$ Sir.")
    elif age > 18:
        bill = 12
        print("Youth tickets are 12$ Sir.")
    else:
        bill = 7
        print("Adult tickets are 7$ Sir.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill ${bill}.")

else:
    # If the height is less than 120 cm, print a message saying the user cannot ride the rollercoaster
    print("Sorry, You can't ride the rollercoaster!")

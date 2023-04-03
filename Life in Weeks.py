# This program calculates the number of days, weeks, and months left until a person reaches the age of 90.
# The user is prompted to enter their current age.
# The program then subtracts the current age from 90 to determine the number of years left.
# The number of years left is then multiplied by 365 to calculate the number of days left, by 52 to calculate the number of weeks left, and by 12 to calculate the number of months left.
# The results are then printed to the console using formatted strings.

# Prompt the user to enter their current age and convert it to an integer
curr_age = int(input("What is your current age: "))

# Set the maximum age to 90
live_age = 90

# Calculate the number of days, weeks, and months left until the user reaches the age of 90
live_days = (live_age - curr_age) * 365
live_weeks = (live_age - curr_age) * 52
live_months = (live_age - curr_age) * 12

# Print the results to the console using formatted strings
print(f"You have {live_days} days, {live_weeks} weeks, and {live_months} months left.")


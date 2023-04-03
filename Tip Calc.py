# This program calculates the amount each person should pay for a restaurant bill including tip and split among a group.
# The user is prompted to enter the total bill, percentage tip, and number of people to split the bill.
# The program then calculates the amount each person should pay and rounds it to two decimal places.
# The result is printed to the console using a formatted string.

# Welcome message
print("Welcome to the tip calculator.")

# Prompt the user to enter the total bill and convert it to a float
bill = float(input("What is the total bill? ₹"))

# Prompt the user to enter the percentage tip and round it to two decimal places
tip = round(float(input("What percentage tip would you like to give? ")), 2)

# Prompt the user to enter the number of people to split the bill and convert it to an integer
people = int(input("How many people to split the bill? "))

# Calculate the amount each person should pay, including tip and split among the group
p_pay = bill * tip / 100
p_pay = bill + p_pay
p_pay = round(p_pay / people, 2)

# Print the result to the console using a formatted string
print(f"Each person should pay: {p_pay}₹")

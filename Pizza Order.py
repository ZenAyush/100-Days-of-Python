# This program calculates the bill for a pizza delivery based on the size of the pizza and toppings requested by the customer.

print("Welcome to Python Pizza Deliveries!")

# Get user input for pizza size, pepperoni and extra cheese
size = input("What size pizza do you want? S, M, or L ")
add_pepo = input("Do you want pepperoni? Y or N ")
extra_chee = input("Do you want extra cheese? Y or N ")

# Initialize bill to zero
bill = 0

# Calculate bill based on pizza size and toppings
if size == "S":
    bill += 15
    if add_pepo == "Y":
        bill += 2

elif size == "M":
    bill += 20
    if add_pepo == "Y":
        bill += 3

else:
    bill += 25
    if add_pepo == "Y":
        bill += 3

if extra_chee == "Y":
    bill += 1

# Print the final bill to the user
print(f"Your final bill is ${bill}.")
# This program generates a password using letters, numbers, and symbols.
import random

# Lists of possible letters, numbers, and symbols.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Ask user for the number of letters, numbers, and symbols to include in the password.
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

pass_list = []

# Add random letters to the password.
for char in range(1, nr_letters + 1):
    pass_list += random.choice(letters)

# Add random symbols to the password.
for char in range(1, nr_symbols +1):
    pass_list += random.choice(symbols)

# Add random numbers to the password.
for char in range(1, nr_numbers +1):
    pass_list += random.choice(numbers)

# Shuffle the password to randomize the order of characters.
random.shuffle(pass_list)

# Combine the characters in the password list to form the password string.
password = ""
for char in pass_list:
    password += char

# Print the password.
print(f"Your password is: {password}")

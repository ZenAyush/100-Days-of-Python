# Importing the random module for generating random numbers
import random

# Asking the user to input a string of names separated by commas
names_string = input("Give me everybody's names, separated by a comma.")

# Splitting the string into a list of names
names = names_string.split(",")

# Getting the length of the list of names
lent = len(names)

# Generating a random number between 0 and the length of the list of names minus 1
num = random.randint(0, lent-1)

# Printing the name at the index of the randomly generated number
print(names[num]+" is going to buy the meal today!")
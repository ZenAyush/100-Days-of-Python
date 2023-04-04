# Importing the random module to generate random numbers
import random

# Generating a random integer between 0 and 1 to represent heads or tails
random_side = random.randint(0, 1)

# Checking if the random integer is 1, if yes then printing "Heads", else printing "Tails"
if random_side == 1:
    print("Heads")
else:
    print("Tails")

import random

# Generate a random integer between 1 and 10 and assign it to the variable random_interger.
random_interger = random.randint(1,10)
print(random_interger)

# Generate a random float between 0 and 5 and assign it to the variable randomFloat.
randomFloat = random.random() * 5
print(randomFloat)

# Generate a random integer between 1 and 100 and assign it to the variable love_score.
love_score = random.randint(1,100)

# Print a message with the love score.
print(f"Your love score is {love_score}")
# This program calculates the love compatibility between two people based on their names
# The program asks for the names of the two people and then calculates a love score based on the number of times the letters in "true love" appear in their combined names

# Ask for the names of the two people
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Combine the names and convert to lowercase
combo_n = name1.lower() + name2.lower()

# Count the number of times the letters in "true" appear in the combined name
t = combo_n.count("t")
r = combo_n.count("r")
u = combo_n.count("u")
e = combo_n.count("e")
true = t+r+u+e

# Count the number of times the letters in "love" appear in the combined name
l = combo_n.count("l")
o = combo_n.count("o")
v = combo_n.count("v")
e = combo_n.count("e")
love = l+o+v+e

# Calculate the love score by combining the number of "true" and "love" occurrences
love_score = str(true)+str(love)

# Determine the love compatibility based on the love score
if love_score < "10" or love_score > "90":
    print(f"Your score is {love_score}, you go together like code and mentos.")
elif love_score >= "40" and love_score <= "50":
    print(f"Your score is {love_score}, your are alright together.")
else:
    print("Your score is "+love_score)
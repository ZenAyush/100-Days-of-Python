# Prompt the user to enter their height in metershei = input('Enter your height in m: ')
# Prompt the user to enter their weight in kilograms
wei = input('Enter your weight in kg: ')

# Prompt the user to enter their height in meters
hei = input('Enter your height in m: ')

# Calculate the BMI using the input values
# Convert the weight to an integer and the height to a float
bmi = int(wei) / float(hei) ** 2

# Print the calculated BMI as an integer
print(int(bmi))
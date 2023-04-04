# Prompt the user to enter their height in metershei = input('Enter your height in m: ')
# Prompt the user to enter their weight in kilograms
wei = input('Enter your weight in kg: ')

# Prompt the user to enter their height in meters
hei = input('Enter your height in m: ')

# Calculate the BMI using the input values
# Convert the weight to an integer and the height to a float
bmi = round(int(wei) / float(hei) ** 2)

# Check BMI and print message
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have normal weight.")
elif bmi < 30:
    print("You are overweight.")
elif bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")

# Print the calculated BMI as an integer
print(f"Your BMI {bmi}")
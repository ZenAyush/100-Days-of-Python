# Ask the user to input a list of scores separated by spaces
student_scores = input("Input a list of scores separated by spaces: ").split()

# Convert each element in the list from a string to an integer
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Find the maximum value in the list
max = student_scores[0]
for score in student_scores:
    if score > max:
        max = score

# Print the maximum value
print(f"The highest score in the class is: {max}")

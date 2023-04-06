# Ask the user to input a list of student heights separated by spaces
student_heights = input("Input a list of student heights separated by spaces: ").split()

# Convert the input to a list of integers
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Print the list of student heights
print(student_heights)

# Calculate the average height of the students
sum = 0  # initialize the sum of heights to zero
list_len = 0  # initialize the length of the list to zero

# Iterate over the list of heights and add them up
for height in student_heights:
    sum += height
    list_len =+ 1

# Calculate the average height
avg = int(sum/list_len)

# Print the average height
print(f"Average student height is: {avg}")

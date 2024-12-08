# Input: Accept an integer number n
n = int(input("Enter an integer: "))

# Create an empty dictionary
square_dict = {}

# Loop through numbers from 1 to n
for i in range(1, n + 1):
    square_dict[i] = i * i  # Add key-value pair to the dictionary

# Print the dictionary
print(square_dict)

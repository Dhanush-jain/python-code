# Accept a string from the user
text = input("Enter a string: ")

# Convert lowercase to uppercase and vice versa
lower_to_upper = text.lower()  # Convert to lowercase
upper_to_lower = text.upper()  # Convert to uppercase

# Swap the case
swapped_case = text.swapcase()  # Swap the case

# Print the results
print(f"Lowercase to Uppercase: {upper_to_lower}")
print(f"Uppercase to Lowercase: {lower_to_upper}")
print(f"Swapped case: {swapped_case}")

import math

# Fixed values of C and H
C = 50
H = 30

# Input values of D
input_values = input("Enter values of D (comma-separated): ")
D_values = input_values.split(",")  # Split input into a list of strings

results = []
for D in D_values:
    D = int(D)  # Convert each D value to an integer
    Q = math.sqrt((2 * C * D) / H)  # Calculate Q
    results.append(round(Q))  # Round the result and add to the list

# Print results as a comma-separated string
print("Output:", ",".join(map(str, results)))

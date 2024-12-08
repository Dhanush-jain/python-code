n = int(input("Enter a positive integer: "))
if n > 0:
    # Calculate sum using the formula
    total_sum = (n * (n + 1)) / 2
    # Calculate average
    average = total_sum / n
    print(f"The sum of the first {n} natural numbers is: {total_sum}")
    print(f"The average of the first {n} natural numbers is: {average}")
else:
    print("Please enter a positive integer.")

def sum_and_list_of_numbers(start, end):
    even_numbers = []
    odd_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers

# Input range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Get even and odd numbers
even_numbers, odd_numbers = sum_and_list_of_numbers(start, end)

# Print results
print(f"Even numbers: {even_numbers}")
print(f"Sum of even numbers: {sum(even_numbers)}")
print(f"Odd numbers: {odd_numbers}")
print(f"Sum of odd numbers: {sum(odd_numbers)}")

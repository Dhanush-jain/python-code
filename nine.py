n = int(input("Enter the number of records: "))
records = []

# Input data for each record
for _ in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height: "))
    records.append((name, age, height))

# Sort the records based on name, age, and height
records.sort()

# Display the sorted records
print("\nSorted records:")
for record in records:
    print(record)

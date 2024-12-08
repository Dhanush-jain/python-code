# Initialize an empty list to store student details
students = []

# Loop to get details of three students
for i in range(3):
    print(f"Enter details for student {i + 1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    average_score = float(input("Average Score: "))
    
    # Create a tuple with student details and add it to the list
    student = (name, age, average_score)
    students.append(student)

# Print the list of tuples
print("\nList of students:")
print(students)

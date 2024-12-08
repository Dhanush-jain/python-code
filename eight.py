# Get the filename from the user
filename = input("Enter the name of the text file (with extension): ")

# Check if the file exists
file = open(filename, 'r') if filename else None

if file:
    # Read the content and count the number of words
    content = file.read()
    words = content.split()  # Split content into words
    print(f"Number of words in the file: {len(words)}")
    file.close()  # Close the file after reading
else:
    print("File not found.")

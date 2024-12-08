def count_case(sentence):
    upper_count = 0
    lower_count = 0

    # Loop through each character in the sentence
    for char in sentence:
        if char.isupper():
            upper_count += 1  # Increment for uppercase letters
        elif char.islower():
            lower_count += 1  # Increment for lowercase letters

    print("Number of uppercase letters:", upper_count)
    print("Number of lowercase letters:", lower_count)

# Accept a sentence from the user
user_input = input("Enter a sentence: ")
count_case(user_input)

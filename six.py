# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Print the frequency of each word
for word in set(words):
    print(f"{word}: {words.count(word)}")

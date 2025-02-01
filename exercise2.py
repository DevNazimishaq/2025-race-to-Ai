alure="Nazimishaq"
print(alure.count('N'))
# how ai did it
# Take input from the user
user_string = input("Enter a string: ")
letter = input("Enter the letter to count: ")

# Count occurrences (case-insensitive)
count = user_string.lower().count(letter.lower())

# Display the result
print(f"The letter '{letter}' appears {count} time(s) in the string.")
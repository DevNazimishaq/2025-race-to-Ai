name= input(str())
print("Your input is",name)
print(name.upper())
print(name.replace('\t','_'))
      
# how ai does it
# Take input from the user
user_string = input("Enter a string: ")

# Convert to uppercase
upper_case_string = user_string.upper()

# Replace spaces with underscores
final_string = upper_case_string.replace(" ", "_")

# Display the result
print("Transformed string:", final_string)

"""Write a program that:
Asks the user for a number.
Prints all even numbers from 1 to that number using a for loop."""

# x=int(input("Enter your number: "))
# i=1
# for i in range:(i,x+1):
# if 
# print(x)
# Take input from the user
number = int(input("Enter a number: "))

# Loop through numbers from 1 to the given number
print("Even numbers:")
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i)

# multiplication table
# Take input from the user
num = int(input("Enter a number for the multiplication table: "))

# Initialize a counter
i = 1

# Use a while loop to generate the table
print(f"Multiplication table for {num}:")
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

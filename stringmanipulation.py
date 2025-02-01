# string opertaions,
# 1. concatenation
print("Hello"+ "hello")
# 2.Repetition
print("Hello" *3)
# 3.Indexing
print("Hello"[0])
# 4. slicing
print("Hello"[0:3])
# 5. lenght
print (len("Hello"))
# string Methods
# lower()	Converts string to lowercase	"PYTHON".lower()	"python"
# upper()	Converts string to uppercase	"python".upper()	"PYTHON"
# strip()	Removes leading/trailing spaces	" hello ".strip()	"hello
# replace()	Replaces a substring with another	"hello".replace('l', 'p')	"heppo"
# split()	Splits string into a list	"a,b,c".split(',')	['a', 'b', 'c']
# join()	Joins a list into a string	" ".join(['Hello', 'World'])	"Hello World"
# find()	Returns index of first occurrence	"hello".find('l')	2
# count()	Counts occurrences of a substring

print("FURKAN".lower())
print("furkan".upper())
print("furkan ".strip())
print("furkan".replace('f','t'))
print("furkan".split('f''u''r'))
print("furkan".join(['f','u']))
print("furkan".find('k'))
print("furkan".count('f'))
# escape characters
print("He said \'Hi")#single quote
print("He said \"Hi\"")#double quote
print("Hello\nWorld")#newline
print("Hello\tWorld")#tab
# string formatting
name = "Furkan"
age = 25
print(f"My name is {name} and I am {age} years old.")# using f-strings formatting
course="B.tech cse"
Batch=2023
print(f"I am pursuing {course} and my batch {Batch} is.")
print("My name is {} and I am {} years old.".format(name, age))#.format 
print("My name is %s and I am %d years old." % (name, age))#old style




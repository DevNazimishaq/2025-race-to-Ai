# if condition:
#     Code to execute if condition is True
# elif another_condition:
#     Code to execute if another_condition is True
# else:
#     Code to execute if all conditions are False

# example first if statement
age=16
if age>=18:
    print("you are an adult !")  

# example 2nd if-else
num=5
if num % 2==0:
    print("even number")
else:
    print("odd number")  

# example 3rd if-elif-else  
marks=int(input("Enter your Marks: "))
if marks>=95:
    print("grade A")
elif marks>=75:
    print("Grade B")
elif marks>95:
    print("YAY! you are topper")    
elif marks<50:
    print("you are a Mond kath")    
else:
    print("Grade C")        
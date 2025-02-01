# learning basic operators in python
# 1.Arthimetic operators
a = 10
b = 3
print("Addition:", a + b)         # 13
print("Division:", a / b)         # 3.333...
print("Floor Division:", a // b) # 3
print("Exponentiation:", a ** b) # 1000
# 2.comparisn operators
# # These compare two values and return True or False.
# Operator	Description	Example
# ==	Equal to	5 == 3 = False
# !=	Not equal to	5 != 3 = True
# >	Greater than	5 > 3 = True
# <	Less than	5 < 3 = False
# >=	Greater than or equal to	5 >= 3 = True
# <=	Less than or equal to	5 <= 3 = False
a=4
b=6
print("equal to",a==b)
print("equal to",a!=b)
print("equal to",a>b)
print("equal to",a>b)
print("equal to",a<b)
print("equal to",a>=b)
print("equal to",a<=b)

# 3.logical operators
# Operator	Description	Example
# and	Returns True if both conditions are true	(5 > 3) and (7 > 5) = True
# or	Returns True if at least one condition is true	(5 > 3) or (5 < 3) = True
# not	Reverses the result	not(5 > 3) = False
a=5
b=4
c=6
d=2
print("and opertor",a>b and c>d)
print("or opertor",a<b or c>d)
print("not opertor",not a<b)

# 4. Assignment Operators
# These assign values to variables.

# Operator	Example	Equivalent To
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# //=	x //= 3	x = x // 3
# %=	x %= 3	x = x % 3
# **=	x **= 3	x = x ** 3
a = 10
a += 3
a-= 3
a*= 3
print("all the assignment operations of a are", a)
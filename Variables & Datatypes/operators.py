# Following are some common operators in Python
a = 10
b = 20

# 1. Arithmetic operators: +, -, *, / etc.
print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division

# 2. Assignment operators: =, +=, -= etc.
a = b          # Assign b to a
print(a)

a += b         # a = a + b
print(a)

a -= b         # a = a - b
print(a)

print(a == b)  # Comparison (not an assignment operator)

# 3. Comparison operators: ==, >, >=, <, != etc.
print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a != b)

# 4. Logical operators: and, or, not
print(a > 10 and b > 10)
print(a > 10 or b < 10)
print(not(a == b))

# --> TRUTH TABLE [ OR ]
# print("True or False is: " , True or False)
# print("True or True is: " , True or True)
# print("False or True is: " , False or True)
# print("False or False is: " , False or False)

# --> AND
# print("True and False is: " , True and False)
# print("True and True is: " , True and True)
# print("False and True is: " , False and True)
# print("False and False is: " , False and False)
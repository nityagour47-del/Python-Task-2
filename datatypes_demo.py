
# Integer
age = 20
print("Age:", age, type(age))

# Float
height = 5.4
print("Height:", height, type(height))

# String
name = "Nitya"
print("Name:", name, type(name))

# Boolean
is_student = True
print("Is Student:", is_student, type(is_student))

# Arithmetic operations
a = 10
b = 3
print("Addition:", a + b)
print("Multiplication:", a * b)

# Type conversion
num_str = "25"
num_int = int(num_str)
num_float = float(num_str)

print("String to Int:", num_int, type(num_int))
print("String to Float:", num_float, type(num_float))

# Error handling
try:
    invalid = int("abc")
except ValueError:
    print("Invalid input handled")

# String concatenation
print("My age is " + str(age))

# Dynamic typing
x = 10
print("x =", x, type(x))

x = "Python"
print("x =", x, type(x))

# -------------------------------
# Exercise 1:
# Write a program that prints "Hello World"
# -------------------------------  

print("Hello World")


# -------------------------------
# Exercise 2:
# Ask the user for their name and print a greeting
# Example: Hello Sarah
# -------------------------------
name = input("who are you??")
print("Hello", name)

# -------------------------------
# Exercise 3:
# Calculate the area of a rectangle
# The user enters length and width
# -------------------------------
length = input("length=")
l = int(length)
width = input("width=")
w = int(width)
print("Area=", l * w)

# -------------------------------
# Exercise 4:
# Convert temperature from Celsius to Fahrenheit
# Formula: F = (C * 9/5) + 32
# -------------------------------
Degree = input("degree=")
C = float(Degree)
F = (C * 9/5) + 32
print("Degree in F=", F)

# -------------------------------
# Exercise 5:
# The user enters 3 numbers
# Print their Sum and Average
# -------------------------------
num1 = input("Enter first num")
fi = int(num1)
num2 = input("Enter second num")
s = int(num2)
num3 = input("Enter third num")
th = int(num3)

sum = fi + s + th
avg = (fi + s + th) / 3

print("Sum=", sum)
print("Avg=", avg)

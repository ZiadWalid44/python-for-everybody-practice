# -------------------------------
# Exercise 1:
# Ask the user to enter a number.
# If the number is even → print "Even"
# If the number is odd → print "Odd"
# -------------------------------
number = input("Enter a number: ")
num = int(number)

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# -------------------------------
# Exercise 2:
# Ask the user to enter their age.
# If age < 18 → print "Minor"
# If 18 <= age <= 60 → print "Adult"
# If age > 60 → print "Senior"
# -------------------------------
age = input("Enter your age: ")
ag = int(age)

if ag < 18:
    print("Minor")
elif 18 <= ag <= 60:
    print("Adult")
else:
    print("Senior")


# -------------------------------
# Exercise 3:
# Ask the user to enter two numbers.
# Print the larger number.
# If both are equal → print "Both numbers are equal"
# -------------------------------
number1 = input("Enter first number: ")
num1 = int(number1)

number2 = input("Enter second number: ")
num2 = int(number2)

if num1 > num2:
    print("The bigger number is =", num1)
elif num1 < num2:
    print("The bigger number is =", num2)
else:
    print("Both numbers are equal !!")


# -------------------------------
# Exercise 4:
# Ask the user to enter their exam grade.
# If grade >= 90 → print "Excellent"
# If 70 <= grade < 90 → print "Good"
# If 50 <= grade <= 69 → print "Pass"
# If grade < 50 → print "Fail"
# -------------------------------
Grade = input("Enter your grade: ")
gr = int(Grade)

if gr >= 90:
    print("Excellent")
elif 70 <= gr < 90:
    print("Good")
elif 50 <= gr <= 69:
    print("Pass")
else:
    print("Fail")


# -------------------------------
# Exercise 5 (Challenge):
# Ask the user to enter a year.
# Check if it is a leap year or not.
# Rule:
# - Leap year if divisible by 4,
#   but not divisible by 100,
#   except if divisible by 400.
# -------------------------------
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

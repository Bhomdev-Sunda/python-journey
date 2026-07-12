# f-Strings in Python
print("========== F-STRINGS ==========\n")

# Basic f-String
name = "Bhomdev"
age = 22
print("Basic f-String")
print(f"My name is {name}.")
print(f"I am {age} years old.")

# User Input
student = input("\nEnter your name: ")
city = input("Enter your city: ")
print("\nUser Input")
print(f"Welcome {student}!")
print(f"You live in {city}.")

# Mathematical Expressions
num1 = 20
num2 = 10
print("\nMathematical Expressions")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

# Variables Inside f-Strings
course = "Python"
print("\nVariables")
print(f"Course : {course}")
print(f"Length : {len(course)}")

# String Methods
print("\nString Methods")
print(f"Upper : {course.upper()}")
print(f"Lower : {course.lower()}")
print(f"Title : {course.title()}")

# Number Formatting
price = 1250.56789
print("\nNumber Formatting")
print(f"Original : {price}")
print(f"2 Decimal Places : {price:.2f}")
print(f"3 Decimal Places : {price:.3f}")

# Percentage
marks = 447
total = 500
percentage = (marks / total) * 100
print("\nPercentage")
print(f"Marks : {marks}/{total}")
print(f"Percentage : {percentage:.2f}%")

# Alignment
print("\nAlignment")
print(f"|{'Python':<15}|")
print(f"|{'Python':>15}|")
print(f"|{'Python':^15}|")

# Escape Characters
print("\nEscape Characters")
print(f"Hello\n{name}")
print(f"Python\tProgramming")

# Boolean Values
is_student = True
print("\nBoolean")
print(f"Student : {is_student}")

# Multiple Variables
language = "Python"
version = 3.14
print("\nMultiple Variables")
print(f"{name} is learning {language} {version}.")

# Expressions
print("\nExpressions")
print(f"Square of 5 = {5 ** 2}")
print(f"Cube of 3 = {3 ** 3}")

# Mini Student Report
print("\n========== STUDENT REPORT ==========")
student_name = "Bhomdev"
student_age = 22
student_marks = 92.5
print(f"Name  : {student_name}")
print(f"Age   : {student_age}")
print(f"Marks : {student_marks}")

print("\n========== END ==========")
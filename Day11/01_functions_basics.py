#             Python Functions Basics - Day 11

print("=" * 65)
print("           PYTHON FUNCTIONS BASICS")
print("=" * 65)

# ==========================================================
# WHAT IS A FUNCTION?
# ==========================================================

# A function is a block of reusable code that performs
# a specific task.

# Syntax:
#
# def function_name():
#     statements
#
# function_name()

# ==========================================================
# EXAMPLE 1 - SIMPLE FUNCTION
# ==========================================================

print("\n" + "=" * 65)
print("1. SIMPLE FUNCTION")
print("=" * 65)

def greet():
    print("Hello, Welcome to Python!")

greet()

# ==========================================================
# EXAMPLE 2 - FUNCTION CALLED MULTIPLE TIMES
# ==========================================================

print("\n" + "=" * 65)
print("2. CALL FUNCTION MULTIPLE TIMES")
print("=" * 65)

def welcome():
    print("Welcome to Day 11 of Python Journey!")

welcome()
welcome()
welcome()

# ==========================================================
# EXAMPLE 3 - FUNCTION TO PRINT A LINE
# ==========================================================

print("\n" + "=" * 65)
print("3. PRINT LINE")
print("=" * 65)

def line():
    print("-" * 50)

line()

print("Python")

line()

print("Functions")

line()

# ==========================================================
# EXAMPLE 4 - FUNCTION WITH ONE PARAMETER
# ==========================================================

print("\n" + "=" * 65)
print("4. FUNCTION WITH ONE PARAMETER")
print("=" * 65)

def greet_user(name):
    print("Hello,", name)

greet_user("Bhomdev")
greet_user("Rahul")
greet_user("Aman")

# ==========================================================
# EXAMPLE 5 - FUNCTION WITH MULTIPLE PARAMETERS
# ==========================================================

print("\n" + "=" * 65)
print("5. MULTIPLE PARAMETERS")
print("=" * 65)

def student(name, age, course):

    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)

student("Bhomdev", 22, "Python")

# ==========================================================
# EXAMPLE 6 - ADDITION FUNCTION
# ==========================================================

print("\n" + "=" * 65)
print("6. ADDITION")
print("=" * 65)

def add(num1, num2):

    result = num1 + num2

    print("Addition :", result)

add(10, 20)

add(50, 30)

# ==========================================================
# EXAMPLE 7 - SUBTRACTION
# ==========================================================

print("\n" + "=" * 65)
print("7. SUBTRACTION")
print("=" * 65)

def subtract(a, b):

    print("Answer :", a - b)

subtract(50, 15)

# ==========================================================
# EXAMPLE 8 - MULTIPLICATION
# ==========================================================

print("\n" + "=" * 65)
print("8. MULTIPLICATION")
print("=" * 65)

def multiply(a, b):

    print("Answer :", a * b)

multiply(8, 5)

# ==========================================================
# EXAMPLE 9 - CHECK EVEN OR ODD
# ==========================================================

print("\n" + "=" * 65)
print("9. EVEN OR ODD")
print("=" * 65)

def check_number(number):

    if number % 2 == 0:
        print(number, "is Even")

    else:
        print(number, "is Odd")

check_number(20)

check_number(17)

# ==========================================================
# EXAMPLE 10 - TABLE OF A NUMBER
# ==========================================================

print("\n" + "=" * 65)
print("10. MULTIPLICATION TABLE")
print("=" * 65)

def table(number):

    for i in range(1, 11):

        print(f"{number} x {i} = {number * i}")

table(5)

# ==========================================================
# EXAMPLE 11 - AREA OF RECTANGLE
# ==========================================================

print("\n" + "=" * 65)
print("11. AREA OF RECTANGLE")
print("=" * 65)

def rectangle_area(length, width):

    area = length * width

    print("Area :", area)

rectangle_area(10, 5)

# ==========================================================
# EXAMPLE 12 - STUDENT REPORT
# ==========================================================

print("\n" + "=" * 65)
print("12. STUDENT REPORT")
print("=" * 65)

def student_report(name, marks):

    print("Student :", name)

    print("Marks   :", marks)

    if marks >= 40:

        print("Result  : Pass")

    else:

        print("Result  : Fail")

student_report("Bhomdev", 92)

student_report("Rahul", 35)

# ==========================================================
# EXAMPLE 13 - SHOP BILL
# ==========================================================

print("\n" + "=" * 65)
print("13. SHOP BILL")
print("=" * 65)

def bill(item, quantity, price):

    total = quantity * price

    print("Item     :", item)

    print("Quantity :", quantity)

    print("Price    :", price)

    print("Total    :", total)

bill("Laptop", 2, 55000)

# ==========================================================
# EXAMPLE 14 - GREETING BY TIME
# ==========================================================

print("\n" + "=" * 65)
print("14. GREETING")
print("=" * 65)

def greeting(name):

    print("Good Morning,", name)

greeting("Bhomdev")

# ==========================================================
# EXAMPLE 15 - FUNCTION INSIDE LOOP
# ==========================================================

print("\n" + "=" * 65)
print("15. FUNCTION INSIDE LOOP")
print("=" * 65)

def stars():

    print("*" * 30)

for i in range(3):

    stars()

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 65)
print("SUMMARY")
print("=" * 65)

print("✔ Function is a reusable block of code.")
print("✔ Functions are created using 'def'.")
print("✔ A function runs only when it is called.")
print("✔ Functions can have parameters.")
print("✔ Parameters receive values called arguments.")
print("✔ Functions help reduce code repetition.")
print("✔ Functions make programs cleaner and easier to maintain.")
print("✔ Functions improve readability and reusability.")

print("=" * 65)
print("End of functions_basics.py")
print("=" * 65)
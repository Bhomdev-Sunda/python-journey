# ==========================================================
#          Python Return Statement - Day 11
# ==========================================================

print("=" * 70)
print("             PYTHON RETURN STATEMENT")
print("=" * 70)

# ==========================================================
# WHAT IS A RETURN STATEMENT?
# ==========================================================

# The return statement is used to send a value
# back from a function to the place where it was called.

# Syntax:
#
# def function_name():
#     return value

# ==========================================================
# EXAMPLE 1 - RETURNING A NUMBER
# ==========================================================

print("\n" + "=" * 70)
print("1. RETURN A NUMBER")
print("=" * 70)

def number():

    return 100

result = number()

print("Returned Value :", result)

# ==========================================================
# EXAMPLE 2 - RETURNING A STRING
# ==========================================================

print("\n" + "=" * 70)
print("2. RETURN A STRING")
print("=" * 70)

def message():

    return "Welcome to Python!"

text = message()

print(text)

# ==========================================================
# EXAMPLE 3 - ADDITION
# ==========================================================

print("\n" + "=" * 70)
print("3. ADDITION")
print("=" * 70)

def add(a, b):

    return a + b

answer = add(25, 35)

print("Addition :", answer)

# ==========================================================
# EXAMPLE 4 - SUBTRACTION
# ==========================================================

print("\n" + "=" * 70)
print("4. SUBTRACTION")
print("=" * 70)

def subtract(a, b):

    return a - b

print("Answer :", subtract(80, 30))

# ==========================================================
# EXAMPLE 5 - MULTIPLICATION
# ==========================================================

print("\n" + "=" * 70)
print("5. MULTIPLICATION")
print("=" * 70)

def multiply(a, b):

    return a * b

result = multiply(12, 5)

print("Answer :", result)

# ==========================================================
# EXAMPLE 6 - DIVISION
# ==========================================================

print("\n" + "=" * 70)
print("6. DIVISION")
print("=" * 70)

def divide(a, b):

    return a / b

print("Answer :", divide(100, 4))

# ==========================================================
# EXAMPLE 7 - EVEN OR ODD
# ==========================================================

print("\n" + "=" * 70)
print("7. EVEN OR ODD")
print("=" * 70)

def check_even(number):

    if number % 2 == 0:
        return "Even"

    else:
        return "Odd"

print("20 is", check_even(20))

print("17 is", check_even(17))

# ==========================================================
# EXAMPLE 8 - LARGEST NUMBER
# ==========================================================

print("\n" + "=" * 70)
print("8. LARGEST NUMBER")
print("=" * 70)

def largest(a, b):

    if a > b:
        return a

    else:
        return b

print("Largest :", largest(80, 45))

# ==========================================================
# EXAMPLE 9 - AREA OF RECTANGLE
# ==========================================================

print("\n" + "=" * 70)
print("9. AREA OF RECTANGLE")
print("=" * 70)

def rectangle_area(length, width):

    return length * width

area = rectangle_area(12, 8)

print("Area :", area)

# ==========================================================
# EXAMPLE 10 - STUDENT RESULT
# ==========================================================

print("\n" + "=" * 70)
print("10. STUDENT RESULT")
print("=" * 70)

def result(marks):

    if marks >= 40:
        return "Pass"

    else:
        return "Fail"

print("Result :", result(82))

print("Result :", result(25))

# ==========================================================
# EXAMPLE 11 - RETURN MULTIPLE VALUES
# ==========================================================

print("\n" + "=" * 70)
print("11. RETURN MULTIPLE VALUES")
print("=" * 70)

def student():

    name = "Bhomdev"

    age = 22

    course = "Python"

    return name, age, course

name, age, course = student()

print("Name   :", name)

print("Age    :", age)

print("Course :", course)

# ==========================================================
# EXAMPLE 12 - RETURN A LIST
# ==========================================================

print("\n" + "=" * 70)
print("12. RETURN A LIST")
print("=" * 70)

def fruits():

    return ["Apple", "Mango", "Orange"]

fruit_list = fruits()

print(fruit_list)

# ==========================================================
# EXAMPLE 13 - RETURN A DICTIONARY
# ==========================================================

print("\n" + "=" * 70)
print("13. RETURN A DICTIONARY")
print("=" * 70)

def employee():

    return {

        "Name": "Rahul",

        "Salary": 50000,

        "Department": "IT"

    }

details = employee()

for key, value in details.items():

    print(f"{key:<12}: {value}")

# ==========================================================
# EXAMPLE 14 - RETURN INSIDE LOOP
# ==========================================================

print("\n" + "=" * 70)
print("14. RETURN INSIDE LOOP")
print("=" * 70)

def first_even(numbers):

    for number in numbers:

        if number % 2 == 0:

            return number

numbers = [7, 9, 11, 18, 25]

print("First Even Number :", first_even(numbers))

# ==========================================================
# EXAMPLE 15 - SHOP BILL
# ==========================================================

print("\n" + "=" * 70)
print("15. SHOP BILL")
print("=" * 70)

def calculate_bill(price, quantity):

    total = price * quantity

    gst = total * 0.18

    final_bill = total + gst

    return final_bill

bill = calculate_bill(500, 3)

print("Final Bill :", bill)

# ==========================================================
# EXAMPLE 16 - RETURN VS PRINT
# ==========================================================

print("\n" + "=" * 70)
print("16. RETURN VS PRINT")
print("=" * 70)

def using_print():

    print("Hello from print")

def using_return():

    return "Hello from return"

using_print()

message = using_return()

print(message)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ return sends a value back to the caller.")
print("✔ A function can return numbers, strings, lists,")
print("  tuples, dictionaries, and more.")
print("✔ return immediately exits the function.")
print("✔ Multiple values can be returned.")
print("✔ Returned values can be stored in variables.")
print("✔ return is different from print().")
print("✔ return makes functions reusable.")
print("✔ Functions without return automatically return None.")

print("=" * 70)
print("End of return_statement.py")
print("=" * 70)
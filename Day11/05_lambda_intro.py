# ==========================================================
#         Python Lambda Functions - Day 11
# ==========================================================

print("=" * 70)
print("            PYTHON LAMBDA FUNCTIONS")
print("=" * 70)

# ==========================================================
# WHAT IS A LAMBDA FUNCTION?
# ==========================================================

# A lambda function is a small anonymous (nameless)
# function that can have any number of arguments
# but only ONE expression.

# Syntax:
#
# lambda arguments : expression

# ==========================================================
# EXAMPLE 1 - SIMPLE LAMBDA
# ==========================================================

print("\n" + "=" * 70)
print("1. SIMPLE LAMBDA")
print("=" * 70)

square = lambda x: x * x

print("Square of 5 :", square(5))

# ==========================================================
# EXAMPLE 2 - ADDITION
# ==========================================================

print("\n" + "=" * 70)
print("2. ADDITION")
print("=" * 70)

add = lambda a, b: a + b

print("10 + 20 =", add(10, 20))

# ==========================================================
# EXAMPLE 3 - SUBTRACTION
# ==========================================================

print("\n" + "=" * 70)
print("3. SUBTRACTION")
print("=" * 70)

subtract = lambda a, b: a - b

print("50 - 15 =", subtract(50, 15))

# ==========================================================
# EXAMPLE 4 - MULTIPLICATION
# ==========================================================

print("\n" + "=" * 70)
print("4. MULTIPLICATION")
print("=" * 70)

multiply = lambda a, b: a * b

print("8 x 7 =", multiply(8, 7))

# ==========================================================
# EXAMPLE 5 - DIVISION
# ==========================================================

print("\n" + "=" * 70)
print("5. DIVISION")
print("=" * 70)

divide = lambda a, b: a / b

print("100 / 5 =", divide(100, 5))

# ==========================================================
# EXAMPLE 6 - EVEN OR ODD
# ==========================================================

print("\n" + "=" * 70)
print("6. EVEN OR ODD")
print("=" * 70)

check = lambda n: "Even" if n % 2 == 0 else "Odd"

print("20 :", check(20))
print("17 :", check(17))

# ==========================================================
# EXAMPLE 7 - LARGEST NUMBER
# ==========================================================

print("\n" + "=" * 70)
print("7. LARGEST NUMBER")
print("=" * 70)

largest = lambda a, b: a if a > b else b

print("Largest :", largest(80, 45))

# ==========================================================
# EXAMPLE 8 - STRING LENGTH
# ==========================================================

print("\n" + "=" * 70)
print("8. STRING LENGTH")
print("=" * 70)

length = lambda text: len(text)

print("Length :", length("Python"))

# ==========================================================
# EXAMPLE 9 - UPPERCASE
# ==========================================================

print("\n" + "=" * 70)
print("9. UPPERCASE")
print("=" * 70)

upper = lambda text: text.upper()

print(upper("bhomdev"))

# ==========================================================
# EXAMPLE 10 - map()
# ==========================================================

print("\n" + "=" * 70)
print("10. map()")
print("=" * 70)

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("Original :", numbers)

print("Squares  :", squares)

# ==========================================================
# EXAMPLE 11 - filter()
# ==========================================================

print("\n" + "=" * 70)
print("11. filter()")
print("=" * 70)

numbers = [10, 15, 20, 25, 30, 35]

even = list(filter(lambda x: x % 2 == 0, numbers))

print("Original :", numbers)

print("Even     :", even)

# ==========================================================
# EXAMPLE 12 - sorted()
# ==========================================================

print("\n" + "=" * 70)
print("12. sorted()")
print("=" * 70)

students = [

    ("Rahul", 75),

    ("Bhomdev", 92),

    ("Aman", 65),

    ("Priya", 88)

]

sorted_students = sorted(students, key=lambda student: student[1])

print("Sorted by Marks")

for student in sorted_students:

    print(student)

# ==========================================================
# EXAMPLE 13 - SORT BY NAME
# ==========================================================

print("\n" + "=" * 70)
print("13. SORT BY NAME")
print("=" * 70)

sorted_name = sorted(students, key=lambda student: student[0])

for student in sorted_name:

    print(student)

# ==========================================================
# EXAMPLE 14 - REAL-LIFE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("14. PRODUCT DISCOUNT")
print("=" * 70)

products = [

    ("Laptop", 60000),

    ("Mouse", 800),

    ("Keyboard", 1800)

]

discount_price = list(

    map(

        lambda item: (item[0], item[1] * 0.9),

        products

    )

)

for product in discount_price:

    print(product)

# ==========================================================
# EXAMPLE 15 - LAMBDA INSIDE FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("15. LAMBDA INSIDE FUNCTION")
print("=" * 70)

def calculator():

    multiply = lambda a, b: a * b

    return multiply

result = calculator()

print(result(15, 4))

# ==========================================================
# EXAMPLE 16 - MULTIPLE ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("16. MULTIPLE ARGUMENTS")
print("=" * 70)

student = lambda name, age, course: f"{name} | {age} | {course}"

print(student("Bhomdev", 22, "Python"))

# ==========================================================
# EXAMPLE 17 - BOOLEAN RESULT
# ==========================================================

print("\n" + "=" * 70)
print("17. BOOLEAN RESULT")
print("=" * 70)

adult = lambda age: age >= 18

print(adult(22))

print(adult(15))

# ==========================================================
# EXAMPLE 18 - CUBE
# ==========================================================

print("\n" + "=" * 70)
print("18. CUBE")
print("=" * 70)

cube = lambda x: x ** 3

print(cube(5))

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Lambda is an anonymous function.")
print("✔ Lambda uses the 'lambda' keyword.")
print("✔ It can have multiple arguments.")
print("✔ It contains only one expression.")
print("✔ Useful for short functions.")
print("✔ Commonly used with map(), filter(), and sorted().")
print("✔ Makes code shorter and cleaner.")
print("✔ Avoid using lambda for complex logic.")

print("=" * 70)
print("End of lambda_intro.py")
print("=" * 70)
# ==========================================================
#       Python Parameters & Arguments - Day 11
# ==========================================================

print("=" * 70)
print("         PYTHON PARAMETERS & ARGUMENTS")
print("=" * 70)

# ==========================================================
# WHAT ARE PARAMETERS AND ARGUMENTS?
# ==========================================================

# Parameter:
# A variable defined inside the function definition.

# Argument:
# The actual value passed to the function when calling it.

# ==========================================================
# EXAMPLE 1 - SINGLE PARAMETER
# ==========================================================

print("\n" + "=" * 70)
print("1. SINGLE PARAMETER")
print("=" * 70)

def greet(name):
    print("Hello,", name)

greet("Bhomdev")
greet("Rahul")

# ==========================================================
# EXAMPLE 2 - MULTIPLE PARAMETERS
# ==========================================================

print("\n" + "=" * 70)
print("2. MULTIPLE PARAMETERS")
print("=" * 70)

def student(name, age, course):

    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)

student("Bhomdev", 22, "Python")

# ==========================================================
# EXAMPLE 3 - POSITIONAL ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("3. POSITIONAL ARGUMENTS")
print("=" * 70)

def employee(name, salary):

    print("Employee :", name)
    print("Salary   :", salary)

employee("Aman", 50000)

# ==========================================================
# EXAMPLE 4 - KEYWORD ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("4. KEYWORD ARGUMENTS")
print("=" * 70)

employee(salary=65000, name="Bhomdev")

# ==========================================================
# EXAMPLE 5 - DEFAULT ARGUMENT
# ==========================================================

print("\n" + "=" * 70)
print("5. DEFAULT ARGUMENT")
print("=" * 70)

def country(name, country="India"):

    print(name, "belongs to", country)

country("Bhomdev")

country("John", "USA")

# ==========================================================
# EXAMPLE 6 - REQUIRED ARGUMENT
# ==========================================================

print("\n" + "=" * 70)
print("6. REQUIRED ARGUMENT")
print("=" * 70)

def square(number):

    print("Square :", number ** 2)

square(8)

# ==========================================================
# EXAMPLE 7 - *args
# ==========================================================

print("\n" + "=" * 70)
print("7. *args")
print("=" * 70)

def addition(*numbers):

    total = 0

    for num in numbers:
        total += num

    print("Total :", total)

addition(10, 20)

addition(10, 20, 30)

addition(10, 20, 30, 40, 50)

# ==========================================================
# EXAMPLE 8 - **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("8. **kwargs")
print("=" * 70)

def student_info(**details):

    for key, value in details.items():
        print(key.title(), ":", value)

student_info(

    Name="Bhomdev",

    Age=22,

    Course="Python"

)

# ==========================================================
# EXAMPLE 9 - MIXING PARAMETERS
# ==========================================================

print("\n" + "=" * 70)
print("9. MIXED PARAMETERS")
print("=" * 70)

def product(name, price, quantity=1):

    total = price * quantity

    print("Product :", name)
    print("Total   :", total)

product("Mouse", 800)

product("Keyboard", 1500, 2)

# ==========================================================
# EXAMPLE 10 - RETURNING TOTAL
# ==========================================================

print("\n" + "=" * 70)
print("10. BILL CALCULATION")
print("=" * 70)

def bill(price, quantity):

    total = price * quantity

    print("Bill :", total)

bill(250, 3)

# ==========================================================
# EXAMPLE 11 - STUDENT RESULT
# ==========================================================

print("\n" + "=" * 70)
print("11. STUDENT RESULT")
print("=" * 70)

def result(name, marks):

    print("Student :", name)

    print("Marks   :", marks)

    if marks >= 40:
        print("Status  : Pass")

    else:
        print("Status  : Fail")

result("Rahul", 75)

result("Aman", 35)

# ==========================================================
# EXAMPLE 12 - AREA OF RECTANGLE
# ==========================================================

print("\n" + "=" * 70)
print("12. AREA OF RECTANGLE")
print("=" * 70)

def rectangle(length, width):

    print("Area :", length * width)

rectangle(10, 5)

# ==========================================================
# EXAMPLE 13 - TABLE FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("13. MULTIPLICATION TABLE")
print("=" * 70)

def table(number):

    for i in range(1, 11):

        print(f"{number} x {i} = {number*i}")

table(7)

# ==========================================================
# EXAMPLE 14 - AVERAGE OF MARKS
# ==========================================================

print("\n" + "=" * 70)
print("14. AVERAGE USING *args")
print("=" * 70)

def average(*marks):

    total = sum(marks)

    avg = total / len(marks)

    print("Average :", avg)

average(80, 85, 90)

average(65, 70, 75, 80)

# ==========================================================
# EXAMPLE 15 - COMPANY DETAILS
# ==========================================================

print("\n" + "=" * 70)
print("15. COMPANY DETAILS")
print("=" * 70)

def company(**info):

    print("Company Details")

    print("-" * 30)

    for key, value in info.items():

        print(f"{key.title():<12}: {value}")

company(

    Name="Google",

    Location="USA",

    Employees=180000,

    CEO="Sundar Pichai"

)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Parameter → Variable in function definition.")
print("✔ Argument → Actual value passed to the function.")
print("✔ Positional arguments depend on order.")
print("✔ Keyword arguments use parameter names.")
print("✔ Default arguments have predefined values.")
print("✔ *args accepts multiple positional arguments.")
print("✔ **kwargs accepts multiple keyword arguments.")
print("✔ Parameters make functions flexible and reusable.")

print("=" * 70)
print("End of parameters_arguments.py")
print("=" * 70)
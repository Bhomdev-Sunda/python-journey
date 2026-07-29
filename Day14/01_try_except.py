# ==========================================================
#         Python try-except Statement - Day 14
# ==========================================================

print("=" * 70)
print("           PYTHON TRY - EXCEPT")
print("=" * 70)

# ==========================================================
# WHAT IS AN EXCEPTION?
# ==========================================================

# Exception:
# An exception is an error that occurs during program execution.
#
# If we don't handle the exception,
# the program immediately stops.

print("\nAn exception is a runtime error.")
print("Exception handling prevents program crashes.")

# ==========================================================
# WHY DO WE USE TRY-EXCEPT?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE TRY-EXCEPT?")
print("=" * 70)

print("1. Prevent program crashes.")
print("2. Handle runtime errors.")
print("3. Improve user experience.")
print("4. Continue program execution.")
print("5. Build robust applications.")

# ==========================================================
# BASIC TRY-EXCEPT
# ==========================================================

print("\n" + "=" * 70)
print("1. BASIC TRY-EXCEPT")
print("=" * 70)

try:

    number = 10 / 2

    print("Answer :", number)

except:

    print("An error occurred.")

# ==========================================================
# ZERO DIVISION ERROR
# ==========================================================

print("\n" + "=" * 70)
print("2. ZERO DIVISION ERROR")
print("=" * 70)

try:

    number = 10 / 0

    print(number)

except:

    print("Cannot divide by zero.")

# ==========================================================
# VALUE ERROR
# ==========================================================

print("\n" + "=" * 70)
print("3. VALUE ERROR")
print("=" * 70)

try:

    age = int(input("Enter your age : "))

    print("Age :", age)

except:

    print("Please enter a valid number.")

# ==========================================================
# INDEX ERROR
# ==========================================================

print("\n" + "=" * 70)
print("4. INDEX ERROR")
print("=" * 70)

numbers = [10, 20, 30]

try:

    print(numbers[5])

except:

    print("Index does not exist.")

# ==========================================================
# KEY ERROR
# ==========================================================

print("\n" + "=" * 70)
print("5. KEY ERROR")
print("=" * 70)

student = {

    "name": "Bhomdev",
    "course": "Python"

}

try:

    print(student["marks"])

except:

    print("Key not found.")

# ==========================================================
# NAME ERROR
# ==========================================================

print("\n" + "=" * 70)
print("6. NAME ERROR")
print("=" * 70)

try:

    print(city)

except:

    print("Variable is not defined.")

# ==========================================================
# TYPE ERROR
# ==========================================================

print("\n" + "=" * 70)
print("7. TYPE ERROR")
print("=" * 70)

try:

    result = 100 + "Python"

    print(result)

except:

    print("Cannot add integer and string.")

# ==========================================================
# MULTIPLE STATEMENTS
# ==========================================================

print("\n" + "=" * 70)
print("8. TRY BLOCK WITH MULTIPLE STATEMENTS")
print("=" * 70)

try:

    number1 = int(input("Enter First Number : "))
    number2 = int(input("Enter Second Number : "))

    answer = number1 / number2

    print("Result :", answer)

except:

    print("Something went wrong.")

# ==========================================================
# NESTED TRY-EXCEPT
# ==========================================================

print("\n" + "=" * 70)
print("9. NESTED TRY-EXCEPT")
print("=" * 70)

try:

    try:

        number = 20 / 0

    except:

        print("Inner Exception Handled.")

except:

    print("Outer Exception Handled.")

# ==========================================================
# USER LOGIN EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("10. LOGIN EXAMPLE")
print("=" * 70)

correct_password = "python123"

try:

    password = input("Enter Password : ")

    if password == correct_password:

        print("Login Successful!")

    else:

        print("Incorrect Password.")

except:

    print("Login Error.")

# ==========================================================
# SIMPLE CALCULATOR
# ==========================================================

print("\n" + "=" * 70)
print("11. SIMPLE CALCULATOR")
print("=" * 70)

try:

    first = float(input("First Number : "))
    second = float(input("Second Number : "))

    print("Addition :", first + second)
    print("Subtraction :", first - second)
    print("Multiplication :", first * second)
    print("Division :", first / second)

except:

    print("Invalid Input.")

# ==========================================================
# COMMON EXCEPTIONS
# ==========================================================

print("\n" + "=" * 70)
print("COMMON EXCEPTIONS")
print("=" * 70)

exceptions = [

    "ZeroDivisionError",

    "ValueError",

    "TypeError",

    "IndexError",

    "KeyError",

    "NameError",

    "AttributeError",

    "FileNotFoundError",

    "ImportError"

]

for exception in exceptions:

    print("✔", exception)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Using except everywhere.")
print("❌ Ignoring the real error.")
print("❌ Writing empty except blocks.")
print("❌ Not testing user input.")
print("❌ Catching every exception unnecessarily.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "ATM Machine",

    "Online Banking",

    "Student Management",

    "Hospital System",

    "E-Commerce Website",

    "Weather Application",

    "Game Development",

    "File Handling"

]

for app in applications:

    print("✔", app)

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Handle only expected exceptions.")
print("✔ Keep try blocks small.")
print("✔ Write meaningful error messages.")
print("✔ Test user input.")
print("✔ Avoid using bare except in real projects.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ try contains risky code.")
print("✔ except handles runtime errors.")
print("✔ Program continues after handling exceptions.")
print("✔ Prevents application crashes.")
print("✔ Improves user experience.")
print("✔ Makes Python programs more reliable.")

print("=" * 70)
print("End of 01_try_except.py")
print("=" * 70)
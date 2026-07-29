# ==========================================================
#         Common Python Exceptions - Day 14
# ==========================================================

print("=" * 70)
print("            COMMON PYTHON EXCEPTIONS")
print("=" * 70)

# ==========================================================
# WHAT ARE COMMON EXCEPTIONS?
# ==========================================================

# Python has many built-in exceptions.
# These exceptions occur when something goes wrong
# during program execution.

print("\nPython provides many built-in exceptions.")

# ==========================================================
# WHY LEARN COMMON EXCEPTIONS?
# ==========================================================

print("\n" + "=" * 70)
print("WHY LEARN COMMON EXCEPTIONS?")
print("=" * 70)

print("1. Prevent program crashes.")
print("2. Handle user mistakes.")
print("3. Improve debugging.")
print("4. Build reliable applications.")
print("5. Write professional code.")

# ==========================================================
# 1. ZeroDivisionError
# ==========================================================

print("\n" + "=" * 70)
print("1. ZeroDivisionError")
print("=" * 70)

try:

    result = 100 / 0

except ZeroDivisionError as error:

    print(error)

# ==========================================================
# 2. ValueError
# ==========================================================

print("\n" + "=" * 70)
print("2. ValueError")
print("=" * 70)

try:

    age = int("Python")

except ValueError as error:

    print(error)

# ==========================================================
# 3. TypeError
# ==========================================================

print("\n" + "=" * 70)
print("3. TypeError")
print("=" * 70)

try:

    answer = 100 + "Python"

except TypeError as error:

    print(error)

# ==========================================================
# 4. NameError
# ==========================================================

print("\n" + "=" * 70)
print("4. NameError")
print("=" * 70)

try:

    print(city)

except NameError as error:

    print(error)

# ==========================================================
# 5. IndexError
# ==========================================================

print("\n" + "=" * 70)
print("5. IndexError")
print("=" * 70)

numbers = [10, 20, 30]

try:

    print(numbers[5])

except IndexError as error:

    print(error)

# ==========================================================
# 6. KeyError
# ==========================================================

print("\n" + "=" * 70)
print("6. KeyError")
print("=" * 70)

student = {

    "name": "Bhomdev",
    "course": "Python"

}

try:

    print(student["marks"])

except KeyError as error:

    print(error)

# ==========================================================
# 7. AttributeError
# ==========================================================

print("\n" + "=" * 70)
print("7. AttributeError")
print("=" * 70)

text = "Python"

try:

    text.append("AI")

except AttributeError as error:

    print(error)

# ==========================================================
# 8. FileNotFoundError
# ==========================================================

print("\n" + "=" * 70)
print("8. FileNotFoundError")
print("=" * 70)

try:

    file = open("unknown_file.txt", "r")

except FileNotFoundError as error:

    print(error)

# ==========================================================
# 9. ModuleNotFoundError
# ==========================================================

print("\n" + "=" * 70)
print("9. ModuleNotFoundError")
print("=" * 70)

try:

    import abcxyzmodule

except ModuleNotFoundError as error:

    print(error)

# ==========================================================
# 10. ImportError
# ==========================================================

print("\n" + "=" * 70)
print("10. ImportError")
print("=" * 70)

try:

    from math import square_root

except ImportError as error:

    print(error)

# ==========================================================
# 11. OverflowError
# ==========================================================

print("\n" + "=" * 70)
print("11. OverflowError")
print("=" * 70)

try:

    import math

    print(math.exp(1000))

except OverflowError as error:

    print(error)

# ==========================================================
# 12. AssertionError
# ==========================================================

print("\n" + "=" * 70)
print("12. AssertionError")
print("=" * 70)

try:

    age = 15

    assert age >= 18, "Age must be at least 18."

except AssertionError as error:

    print(error)

# ==========================================================
# 13. EOFError
# ==========================================================

print("\n" + "=" * 70)
print("13. EOFError")
print("=" * 70)

print("EOFError usually occurs when input() receives no input.")
print("It is difficult to reproduce in a normal terminal.")

# ==========================================================
# 14. KeyboardInterrupt
# ==========================================================

print("\n" + "=" * 70)
print("14. KeyboardInterrupt")
print("=" * 70)

print("KeyboardInterrupt occurs when you press Ctrl + C.")
print("It cannot be demonstrated automatically.")

# ==========================================================
# 15. Exception (Generic)
# ==========================================================

print("\n" + "=" * 70)
print("15. Generic Exception")
print("=" * 70)

try:

    number = int(input("Enter Number : "))

    print(100 / number)

except Exception as error:

    print("Error :", error)

# ==========================================================
# EXCEPTION HIERARCHY EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("EXCEPTION HIERARCHY")
print("=" * 70)

print("BaseException")
print("   ├── Exception")
print("   │      ├── ValueError")
print("   │      ├── TypeError")
print("   │      ├── NameError")
print("   │      ├── IndexError")
print("   │      ├── KeyError")
print("   │      ├── FileNotFoundError")
print("   │      └── ...")

# ==========================================================
# MOST COMMON EXCEPTIONS
# ==========================================================

print("\n" + "=" * 70)
print("MOST COMMON EXCEPTIONS")
print("=" * 70)

exceptions = [

    "ZeroDivisionError",

    "ValueError",

    "TypeError",

    "NameError",

    "IndexError",

    "KeyError",

    "AttributeError",

    "FileNotFoundError",

    "ModuleNotFoundError",

    "ImportError",

    "OverflowError",

    "AssertionError"

]

for exception in exceptions:

    print("✔", exception)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Ignoring exception messages.")
print("❌ Using except everywhere.")
print("❌ Catching wrong exception type.")
print("❌ Large try blocks.")
print("❌ Not validating user input.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Catch specific exceptions.")
print("✔ Keep try blocks small.")
print("✔ Write meaningful error messages.")
print("✔ Use Exception only when required.")
print("✔ Test invalid inputs.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "ATM Software",

    "Online Banking",

    "Hospital Management",

    "Student Portal",

    "Weather Apps",

    "File Processing",

    "Web Applications",

    "AI & Machine Learning"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Python has many built-in exceptions.")
print("✔ Each exception handles a specific error.")
print("✔ Catch specific exceptions whenever possible.")
print("✔ Avoid generic except unless necessary.")
print("✔ Proper exception handling makes programs reliable.")

print("=" * 70)
print("End of 06_common_exceptions.py")
print("=" * 70)
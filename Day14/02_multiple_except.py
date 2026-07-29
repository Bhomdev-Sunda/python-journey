# ==========================================================
#              02_multiple_except.py
#      Python Multiple Except Blocks - Day 14
# ==========================================================

print("=" * 70)
print("         PYTHON MULTIPLE EXCEPT BLOCKS")
print("=" * 70)

# ==========================================================
# WHAT IS MULTIPLE EXCEPT?
# ==========================================================

# Sometimes a single try block can produce different
# types of exceptions.
#
# Instead of using one generic except block,
# Python allows multiple except blocks to handle
# different exceptions separately.

print("\nMultiple except blocks handle different errors individually.")

# ==========================================================
# WHY USE MULTIPLE EXCEPT?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE MULTIPLE EXCEPT?")
print("=" * 70)

print("1. More readable code.")
print("2. Different message for each error.")
print("3. Easier debugging.")
print("4. Professional coding style.")
print("5. Better user experience.")

# ==========================================================
# ZERO DIVISION ERROR
# ==========================================================

print("\n" + "=" * 70)
print("1. ZeroDivisionError")
print("=" * 70)

try:

    number = 100 / 0

    print(number)

except ZeroDivisionError:

    print("Cannot divide by zero.")

# ==========================================================
# VALUE ERROR
# ==========================================================

print("\n" + "=" * 70)
print("2. ValueError")
print("=" * 70)

try:

    age = int(input("Enter your age : "))

    print("Age :", age)

except ValueError:

    print("Please enter numbers only.")

# ==========================================================
# INDEX ERROR
# ==========================================================

print("\n" + "=" * 70)
print("3. IndexError")
print("=" * 70)

numbers = [10, 20, 30]

try:

    print(numbers[10])

except IndexError:

    print("Index does not exist.")

# ==========================================================
# KEY ERROR
# ==========================================================

print("\n" + "=" * 70)
print("4. KeyError")
print("=" * 70)

student = {

    "name": "Bhomdev",
    "course": "Python"

}

try:

    print(student["marks"])

except KeyError:

    print("Key not found.")

# ==========================================================
# TYPE ERROR
# ==========================================================

print("\n" + "=" * 70)
print("5. TypeError")
print("=" * 70)

try:

    result = 100 + "Python"

    print(result)

except TypeError:

    print("Cannot add integer and string.")

# ==========================================================
# NAME ERROR
# ==========================================================

print("\n" + "=" * 70)
print("6. NameError")
print("=" * 70)

try:

    print(city)

except NameError:

    print("Variable does not exist.")

# ==========================================================
# FILE NOT FOUND ERROR
# ==========================================================

print("\n" + "=" * 70)
print("7. FileNotFoundError")
print("=" * 70)

try:

    file = open("unknown_file.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File not found.")

# ==========================================================
# MULTIPLE EXCEPT IN ONE TRY
# ==========================================================

print("\n" + "=" * 70)
print("8. Multiple Exceptions")
print("=" * 70)

try:

    number = int(input("Enter a number : "))

    result = 100 / number

    print("Answer :", result)

except ValueError:

    print("Invalid number.")

except ZeroDivisionError:

    print("Division by zero is not allowed.")

# ==========================================================
# ANOTHER EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("9. Student Marks Example")
print("=" * 70)

marks = {

    "Python": 95,
    "Java": 90

}

try:

    subject = input("Enter Subject : ")

    print("Marks :", marks[subject])

except KeyError:

    print("Subject not found.")

# ==========================================================
# COMBINING EXCEPTIONS
# ==========================================================

print("\n" + "=" * 70)
print("10. Handling Multiple Exceptions Together")
print("=" * 70)

try:

    number = int(input("Enter Number : "))

    print(100 / number)

except (ValueError, ZeroDivisionError):

    print("Invalid input or division by zero.")

# ==========================================================
# EXCEPTION OBJECT
# ==========================================================

print("\n" + "=" * 70)
print("11. Exception Object")
print("=" * 70)

try:

    number = int("Python")

except ValueError as error:

    print("Error Message :", error)

# ==========================================================
# GENERIC EXCEPTION
# ==========================================================

print("\n" + "=" * 70)
print("12. Generic Exception")
print("=" * 70)

try:

    number = int(input("Enter Number : "))

    print(50 / number)

except Exception as error:

    print("Something went wrong.")

    print("Actual Error :", error)

# ==========================================================
# COMMON EXCEPTIONS
# ==========================================================

print("\n" + "=" * 70)
print("COMMON PYTHON EXCEPTIONS")
print("=" * 70)

exceptions = [

    "ValueError",

    "TypeError",

    "NameError",

    "IndexError",

    "KeyError",

    "ZeroDivisionError",

    "AttributeError",

    "ImportError",

    "ModuleNotFoundError",

    "FileNotFoundError"

]

for item in exceptions:

    print("✔", item)

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Catch specific exceptions.")
print("✔ Keep try blocks small.")
print("✔ Don't hide real errors.")
print("✔ Display meaningful messages.")
print("✔ Use Exception only when necessary.")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Using only 'except:' everywhere.")
print("❌ Catching Exception unnecessarily.")
print("❌ Ignoring exception messages.")
print("❌ Large try blocks.")
print("❌ Wrong exception type.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "ATM Machine",

    "Banking Software",

    "Hospital Management",

    "Student Management",

    "Login Systems",

    "Shopping Websites",

    "Game Development",

    "File Processing"

]

for app in applications:

    print("✔", app)

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ One try block can have multiple except blocks.")
print("✔ Handle each exception separately.")
print("✔ Use specific exceptions whenever possible.")
print("✔ Exception objects provide actual error messages.")
print("✔ Generic Exception should be the last choice.")
print("✔ Multiple except blocks improve code quality.")

print("=" * 70)
print("End of 02_multiple_except.py")
print("=" * 70)
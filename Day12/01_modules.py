# ==========================================================
#             Python Modules - Day 12
# ==========================================================

print("=" * 70)
print("                 PYTHON MODULES")
print("=" * 70)

# ==========================================================
# WHAT IS A MODULE?
# ==========================================================

# A module is a Python file (.py) that contains
# variables, functions, classes, or code that can
# be imported and reused in another Python program.

print("\nA module helps organize and reuse code.")

# ==========================================================
# WHY DO WE USE MODULES?
# ==========================================================

print("\n" + "=" * 70)
print("WHY MODULES ARE USED")
print("=" * 70)

print("1. Code Reusability")
print("2. Better Organization")
print("3. Easier Maintenance")
print("4. Avoid Writing Duplicate Code")
print("5. Improve Readability")

# ==========================================================
# IMPORTING A MODULE
# ==========================================================

print("\n" + "=" * 70)
print("IMPORT MODULE")
print("=" * 70)

import math

print("Square Root of 64 :", math.sqrt(64))
print("Value of Pi       :", math.pi)

# ==========================================================
# IMPORT MULTIPLE MODULES
# ==========================================================

print("\n" + "=" * 70)
print("IMPORT MULTIPLE MODULES")
print("=" * 70)

import random
import datetime

print("Random Number :", random.randint(1, 10))
print("Current Date  :", datetime.date.today())

# ==========================================================
# FROM...IMPORT
# ==========================================================

print("\n" + "=" * 70)
print("FROM...IMPORT")
print("=" * 70)

from math import sqrt, factorial

print("Square Root :", sqrt(81))
print("Factorial   :", factorial(5))

# ==========================================================
# IMPORT AS
# ==========================================================

print("\n" + "=" * 70)
print("IMPORT AS")
print("=" * 70)

import math as m

print("Pi :", m.pi)
print("Power :", m.pow(2, 5))

# ==========================================================
# IMPORT SPECIFIC FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("IMPORT SPECIFIC FUNCTION")
print("=" * 70)

from random import choice

colors = ["Red", "Blue", "Green", "Yellow"]

print("Selected Color :", choice(colors))

# ==========================================================
# USING dir()
# ==========================================================

print("\n" + "=" * 70)
print("dir() FUNCTION")
print("=" * 70)

print("Some functions available in math module:")

print(dir(math)[:15])

# ==========================================================
# MODULE INFORMATION
# ==========================================================

print("\n" + "=" * 70)
print("MODULE INFORMATION")
print("=" * 70)

print("Math Module Name :", math.__name__)

print("Random Module Name :", random.__name__)

# ==========================================================
# __name__ VARIABLE
# ==========================================================

print("\n" + "=" * 70)
print("__name__ VARIABLE")
print("=" * 70)

print("__name__ =", __name__)

if __name__ == "__main__":

    print("This file is running directly.")

else:

    print("This file was imported.")

# ==========================================================
# BUILT-IN MODULES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON BUILT-IN MODULES")
print("=" * 70)

modules = [

    "math",

    "random",

    "datetime",

    "os",

    "sys",

    "time",

    "statistics",

    "calendar",

    "json",

    "collections"

]

for module in modules:

    print(module)

# ==========================================================
# REAL-LIFE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE EXAMPLE")
print("=" * 70)

price = 499.75

print("Original Price :", price)

print("Rounded Price  :", math.ceil(price))

discount = random.randint(5, 25)

print("Today's Discount :", discount, "%")

today = datetime.date.today()

print("Today's Date :", today)

# ==========================================================
# ADVANTAGES OF MODULES
# ==========================================================

print("\n" + "=" * 70)
print("ADVANTAGES")
print("=" * 70)

print("✔ Code Reusability")
print("✔ Better Project Structure")
print("✔ Easy Maintenance")
print("✔ Faster Development")
print("✔ Easy Collaboration")
print("✔ Modular Programming")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to import a module.")
print("❌ Using wrong module names.")
print("❌ Calling functions without module name.")
print("❌ Importing unnecessary modules.")
print("❌ Creating files with the same name as built-in modules.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ A module is a Python file containing reusable code.")
print("✔ Use import to access a module.")
print("✔ Use from...import to import specific functions.")
print("✔ Use import...as to create an alias.")
print("✔ __name__ tells how the file is executed.")
print("✔ Built-in modules save development time.")
print("✔ Modules improve code organization and reusability.")

print("=" * 70)
print("End of modules.py")
print("=" * 70)
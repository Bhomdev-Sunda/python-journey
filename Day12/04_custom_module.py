# ==========================================================
#        Creating and Using a Custom Module - Day 12
# ==========================================================

print("=" * 70)
print("              CUSTOM PYTHON MODULE")
print("=" * 70)

# ==========================================================
# WHAT IS A CUSTOM MODULE?
# ==========================================================

# A custom module is a Python (.py) file created by
# the programmer. It contains reusable functions,
# variables, or classes that can be imported into
# another Python program.

print("\nA custom module is created by the programmer.")

# ==========================================================
# HOW TO CREATE A CUSTOM MODULE
# ==========================================================

print("\n" + "=" * 70)
print("HOW TO CREATE A CUSTOM MODULE")
print("=" * 70)

print("Step 1 : Create a new Python file.")
print("Step 2 : Write functions or variables.")
print("Step 3 : Save the file.")
print("Step 4 : Import it into another Python file.")

# ==========================================================
# EXAMPLE MODULE STRUCTURE
# ==========================================================

print("\n" + "=" * 70)
print("EXAMPLE : my_module.py")
print("=" * 70)

print("""
# my_module.py

college = "ABC College"

def greet(name):
    print("Hello", name)

def add(a, b):
    return a + b
""")

# ==========================================================
# IMPORTING A CUSTOM MODULE
# ==========================================================

print("\n" + "=" * 70)
print("IMPORTING A CUSTOM MODULE")
print("=" * 70)

print("""
import my_module

my_module.greet("Bhomdev")

print(my_module.add(10, 20))

print(my_module.college)
""")

# ==========================================================
# IMPORT SPECIFIC FUNCTIONS
# ==========================================================

print("\n" + "=" * 70)
print("IMPORT SPECIFIC FUNCTIONS")
print("=" * 70)

print("""
from my_module import greet, add

greet("Rahul")

print(add(50, 30))
""")

# ==========================================================
# IMPORT USING ALIAS
# ==========================================================

print("\n" + "=" * 70)
print("IMPORT USING ALIAS")
print("=" * 70)

print("""
import my_module as mm

mm.greet("Aman")

print(mm.add(15, 5))
""")

# ==========================================================
# IMPORT EVERYTHING
# ==========================================================

print("\n" + "=" * 70)
print("IMPORT EVERYTHING")
print("=" * 70)

print("""
from my_module import *

greet("Python")

print(add(5, 7))
""")

print("Note : Avoid 'from module import *' in large projects.")

# ==========================================================
# WHY USE CUSTOM MODULES?
# ==========================================================

print("\n" + "=" * 70)
print("WHY CUSTOM MODULES?")
print("=" * 70)

advantages = [

    "Code Reusability",

    "Better Project Structure",

    "Easy Maintenance",

    "Avoid Duplicate Code",

    "Easy Team Collaboration",

    "Cleaner Programs"

]

for advantage in advantages:

    print("✔", advantage)

# ==========================================================
# PROJECT STRUCTURE
# ==========================================================

print("\n" + "=" * 70)
print("EXAMPLE PROJECT STRUCTURE")
print("=" * 70)

print("""
Project/

│
├── my_module.py
├── main.py
└── README.md
""")

# ==========================================================
# __name__ VARIABLE
# ==========================================================

print("\n" + "=" * 70)
print("__name__ VARIABLE")
print("=" * 70)

print("Current Value of __name__ :", __name__)

if __name__ == "__main__":

    print("This file is running directly.")

else:

    print("This file was imported.")

# ==========================================================
# REAL-LIFE EXAMPLES
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE EXAMPLES")
print("=" * 70)

examples = [

    "Calculator Module",

    "Bank Management Module",

    "Student Management Module",

    "Employee Management Module",

    "Authentication Module",

    "Database Module",

    "Email Module",

    "Utility Module"

]

for example in examples:

    print("-", example)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to save the module file.")
print("❌ Wrong module name while importing.")
print("❌ Keeping module in another folder.")
print("❌ Naming your file the same as a built-in module.")
print("❌ Circular imports (module A imports B and B imports A).")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Keep one purpose per module.")
print("✔ Use meaningful file names.")
print("✔ Group related functions together.")
print("✔ Write comments and documentation.")
print("✔ Use '__name__ == \"__main__\"' for testing.")
print("✔ Avoid unnecessary imports.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ A custom module is created by the programmer.")
print("✔ Modules help organize reusable code.")
print("✔ Import modules using import or from...import.")
print("✔ Aliases can shorten module names.")
print("✔ Use '__name__ == \"__main__\"' to control execution.")
print("✔ Custom modules make projects cleaner and easier to maintain.")

print("=" * 70)
print("End of custom_module.py")
print("=" * 70)
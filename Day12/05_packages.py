# ==========================================================
#          Python Packages Introduction - Day 12
# ==========================================================

print("=" * 70)
print("                PYTHON PACKAGES")
print("=" * 70)

# ==========================================================
# WHAT IS A PACKAGE?
# ==========================================================

# A package is a collection of related Python modules
# organized inside a directory.
#
# A package helps organize large Python projects.

print("\nA package is a folder that contains multiple Python modules.")

# ==========================================================
# WHY DO WE USE PACKAGES?
# ==========================================================

print("\n" + "=" * 70)
print("WHY PACKAGES ARE USED")
print("=" * 70)

print("1. Organize large projects")
print("2. Group related modules")
print("3. Improve readability")
print("4. Easy maintenance")
print("5. Code reusability")
print("6. Better teamwork")

# ==========================================================
# PACKAGE STRUCTURE
# ==========================================================

print("\n" + "=" * 70)
print("PACKAGE STRUCTURE")
print("=" * 70)

print("""
project/

│
├── main.py
│
├── calculator/
│   │
│   ├── __init__.py
│   ├── addition.py
│   ├── subtraction.py
│   ├── multiplication.py
│   └── division.py
│
└── README.md
""")

# ==========================================================
# __init__.py FILE
# ==========================================================

print("\n" + "=" * 70)
print("__init__.py")
print("=" * 70)

print("The '__init__.py' file marks a folder as a Python package.")
print("It can also contain initialization code.")

# ==========================================================
# IMPORTING A PACKAGE
# ==========================================================

print("\n" + "=" * 70)
print("IMPORTING A PACKAGE")
print("=" * 70)

print("""
import calculator.addition

calculator.addition.add(10, 20)
""")

# ==========================================================
# IMPORT SPECIFIC MODULE
# ==========================================================

print("\n" + "=" * 70)
print("IMPORT SPECIFIC MODULE")
print("=" * 70)

print("""
from calculator import addition

addition.add(20, 30)
""")

# ==========================================================
# IMPORT SPECIFIC FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("IMPORT SPECIFIC FUNCTION")
print("=" * 70)

print("""
from calculator.addition import add

print(add(5, 10))
""")

# ==========================================================
# IMPORT USING ALIAS
# ==========================================================

print("\n" + "=" * 70)
print("IMPORT USING ALIAS")
print("=" * 70)

print("""
import calculator.addition as ad

print(ad.add(15, 25))
""")

# ==========================================================
# REAL-WORLD PACKAGE EXAMPLES
# ==========================================================

print("\n" + "=" * 70)
print("POPULAR PYTHON PACKAGES")
print("=" * 70)

packages = [

    "NumPy",

    "Pandas",

    "Matplotlib",

    "Scikit-learn",

    "TensorFlow",

    "OpenCV",

    "Flask",

    "Django",

    "FastAPI",

    "Requests"

]

for package in packages:

    print("✔", package)

# ==========================================================
# STANDARD LIBRARY PACKAGES
# ==========================================================

print("\n" + "=" * 70)
print("STANDARD LIBRARY PACKAGES")
print("=" * 70)

standard_packages = [

    "math",

    "random",

    "datetime",

    "os",

    "sys",

    "json",

    "calendar",

    "statistics",

    "collections",

    "pathlib"

]

for package in standard_packages:

    print("-", package)

# ==========================================================
# PACKAGE VS MODULE
# ==========================================================

print("\n" + "=" * 70)
print("PACKAGE VS MODULE")
print("=" * 70)

print("Module  : A single Python (.py) file.")

print("Package : A folder containing multiple modules.")

# ==========================================================
# ADVANTAGES OF PACKAGES
# ==========================================================

print("\n" + "=" * 70)
print("ADVANTAGES")
print("=" * 70)

advantages = [

    "Better project organization",

    "Easy code reuse",

    "Simple maintenance",

    "Scalable applications",

    "Easy collaboration",

    "Cleaner code structure"

]

for advantage in advantages:

    print("✔", advantage)

# ==========================================================
# REAL-LIFE EXAMPLES
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE EXAMPLES")
print("=" * 70)

examples = [

    "Bank Management System",

    "Hospital Management System",

    "E-commerce Website",

    "Student Management System",

    "Inventory Management",

    "Library Management",

    "Machine Learning Project",

    "Web Development Project"

]

for example in examples:

    print("-", example)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting __init__.py (older Python versions).")
print("❌ Wrong folder structure.")
print("❌ Incorrect import statements.")
print("❌ Circular imports.")
print("❌ Naming packages with built-in module names.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Keep related modules together.")
print("✔ Use meaningful package names.")
print("✔ Avoid unnecessary imports.")
print("✔ Keep package structure clean.")
print("✔ Write documentation.")
print("✔ Follow Python naming conventions.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ A package is a collection of related modules.")
print("✔ Packages help organize large projects.")
print("✔ Modules are Python files.")
print("✔ Packages are folders containing modules.")
print("✔ __init__.py identifies a package.")
print("✔ Packages improve code organization and maintenance.")
print("✔ Large Python applications rely heavily on packages.")

print("=" * 70)
print("End of packages.py")
print("=" * 70)
# ==========================================================
#         Python Import Methods - Day 12
# ==========================================================

print("=" * 70)
print("             PYTHON IMPORT METHODS")
print("=" * 70)

# ==========================================================
# WHAT ARE IMPORT METHODS?
# ==========================================================

# Python provides different ways to import modules.
#
# 1. import module
# 2. import module as alias
# 3. from module import function
# 4. from module import *
#
# Each method has its own use case.

# ==========================================================
# METHOD 1 - import module
# ==========================================================

print("\n" + "=" * 70)
print("1. import module")
print("=" * 70)

import math

print("Square Root of 81 :", math.sqrt(81))
print("Pi Value          :", math.pi)
print("Factorial of 5    :", math.factorial(5))

# ==========================================================
# METHOD 2 - import module as alias
# ==========================================================

print("\n" + "=" * 70)
print("2. import module as alias")
print("=" * 70)

import random as rd

print("Random Number :", rd.randint(1, 100))
print("Random Float  :", rd.random())

# ==========================================================
# METHOD 3 - from module import function
# ==========================================================

print("\n" + "=" * 70)
print("3. from module import function")
print("=" * 70)

from math import sqrt, ceil, floor

print("Square Root :", sqrt(144))
print("Ceil Value  :", ceil(12.25))
print("Floor Value :", floor(12.99))

# ==========================================================
# METHOD 4 - IMPORT MULTIPLE FUNCTIONS
# ==========================================================

print("\n" + "=" * 70)
print("4. Import Multiple Functions")
print("=" * 70)

from math import factorial, gcd

print("Factorial :", factorial(6))
print("GCD       :", gcd(24, 36))

# ==========================================================
# METHOD 5 - from module import *
# ==========================================================

print("\n" + "=" * 70)
print("5. from module import *")
print("=" * 70)

# Not recommended for large projects.
# Used only for learning.

from math import *

print("Square Root :", sqrt(64))
print("Power       :", pow(2, 6))
print("Pi          :", pi)

# ==========================================================
# METHOD 6 - IMPORT datetime MODULE
# ==========================================================

print("\n" + "=" * 70)
print("6. Import datetime")
print("=" * 70)

import datetime

today = datetime.date.today()

print("Today's Date :", today)

print("Current Time :", datetime.datetime.now())

# ==========================================================
# METHOD 7 - FROM datetime IMPORT date
# ==========================================================

print("\n" + "=" * 70)
print("7. from datetime import date")
print("=" * 70)

from datetime import date

print("Today's Date :", date.today())

# ==========================================================
# METHOD 8 - IMPORT time MODULE
# ==========================================================

print("\n" + "=" * 70)
print("8. Import time Module")
print("=" * 70)

import time

print("Current Timestamp :", time.time())

# ==========================================================
# METHOD 9 - IMPORT statistics MODULE
# ==========================================================

print("\n" + "=" * 70)
print("9. Import statistics")
print("=" * 70)

import statistics

numbers = [10, 20, 30, 40, 50]

print("Mean :", statistics.mean(numbers))
print("Median :", statistics.median(numbers))

# ==========================================================
# METHOD 10 - IMPORT calendar MODULE
# ==========================================================

print("\n" + "=" * 70)
print("10. Import calendar")
print("=" * 70)

import calendar

print("Current Year Calendar")

print(calendar.calendar(2026))

# ==========================================================
# METHOD 11 - USING dir()
# ==========================================================

print("\n" + "=" * 70)
print("11. dir() Function")
print("=" * 70)

print("First 20 Functions in math Module")

print(dir(math)[:20])

# ==========================================================
# METHOD 12 - MODULE NAME
# ==========================================================

print("\n" + "=" * 70)
print("12. __name__ Attribute")
print("=" * 70)

print("Math Module :", math.__name__)

print("Random Module :", rd.__name__)

# ==========================================================
# METHOD 13 - REAL-LIFE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("13. Real-Life Example")
print("=" * 70)

price = 3499.99

discount = rd.randint(5, 20)

final_price = price - (price * discount / 100)

print("Original Price :", price)

print("Discount :", discount, "%")

print("Final Price :", round(final_price, 2))

# ==========================================================
# METHOD 14 - __name__ == "__main__"
# ==========================================================

print("\n" + "=" * 70)
print("14. __name__ Example")
print("=" * 70)

if __name__ == "__main__":

    print("This file is executed directly.")

else:

    print("This file is imported.")

# ==========================================================
# IMPORT METHODS COMPARISON
# ==========================================================

print("\n" + "=" * 70)
print("IMPORT METHODS COMPARISON")
print("=" * 70)

print("1. import math")
print("   -> math.sqrt(25)")

print()

print("2. import math as m")
print("   -> m.sqrt(25)")

print()

print("3. from math import sqrt")
print("   -> sqrt(25)")

print()

print("4. from math import *")
print("   -> sqrt(25)")
print("   -> Not recommended in professional projects.")

# ==========================================================
# ADVANTAGES
# ==========================================================

print("\n" + "=" * 70)
print("ADVANTAGES")
print("=" * 70)

print("✔ Reuse existing code")
print("✔ Reduce development time")
print("✔ Organize projects")
print("✔ Improve readability")
print("✔ Easy maintenance")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to import a module.")
print("❌ Using wrong module names.")
print("❌ Using from module import * in large projects.")
print("❌ Naming your file math.py or random.py.")
print("❌ Calling functions without importing them.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ import module")
print("✔ import module as alias")
print("✔ from module import function")
print("✔ from module import *")
print("✔ dir() shows module contents.")
print("✔ __name__ identifies execution mode.")
print("✔ Prefer importing only what you need.")

print("=" * 70)
print("End of import_methods.py")
print("=" * 70)
# ==========================================================
#      Python Math, Random & Datetime Modules - Day 12
# ==========================================================

print("=" * 70)
print("        MATH, RANDOM & DATETIME MODULES")
print("=" * 70)

# ==========================================================
# IMPORT MODULES
# ==========================================================

import math
import random
import datetime

# ==========================================================
# MATH MODULE
# ==========================================================

print("\n" + "=" * 70)
print("1. MATH MODULE")
print("=" * 70)

number = 25

print("Square Root :", math.sqrt(number))
print("Power (5^3) :", math.pow(5, 3))
print("Absolute    :", abs(-50))
print("Ceil        :", math.ceil(12.2))
print("Floor       :", math.floor(12.9))
print("Factorial   :", math.factorial(5))
print("GCD         :", math.gcd(24, 36))
print("Pi          :", math.pi)
print("Euler (e)   :", math.e)

# ==========================================================
# TRIGONOMETRIC FUNCTIONS
# ==========================================================

print("\n" + "=" * 70)
print("2. TRIGONOMETRIC FUNCTIONS")
print("=" * 70)

angle = math.radians(30)

print("sin(30°) :", round(math.sin(angle), 2))
print("cos(30°) :", round(math.cos(angle), 2))
print("tan(30°) :", round(math.tan(angle), 2))

# ==========================================================
# LOG FUNCTIONS
# ==========================================================

print("\n" + "=" * 70)
print("3. LOG FUNCTIONS")
print("=" * 70)

print("Natural Log of 10 :", round(math.log(10), 2))
print("Log Base 10 of 100 :", math.log10(100))

# ==========================================================
# RANDOM MODULE
# ==========================================================

print("\n" + "=" * 70)
print("4. RANDOM MODULE")
print("=" * 70)

print("Random Integer (1-100) :", random.randint(1, 100))
print("Random Float           :", random.random())
print("Random Number (10-20)  :", random.uniform(10, 20))

# ==========================================================
# RANDOM CHOICE
# ==========================================================

print("\n" + "=" * 70)
print("5. RANDOM CHOICE")
print("=" * 70)

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

print("Random Fruit :", random.choice(fruits))

# ==========================================================
# RANDOM SAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("6. RANDOM SAMPLE")
print("=" * 70)

numbers = [10, 20, 30, 40, 50, 60]

print("Random Sample :", random.sample(numbers, 3))

# ==========================================================
# RANDOM SHUFFLE
# ==========================================================

print("\n" + "=" * 70)
print("7. RANDOM SHUFFLE")
print("=" * 70)

cards = ["A", "K", "Q", "J", "10"]

print("Before Shuffle :", cards)

random.shuffle(cards)

print("After Shuffle  :", cards)

# ==========================================================
# DATETIME MODULE
# ==========================================================

print("\n" + "=" * 70)
print("8. DATETIME MODULE")
print("=" * 70)

today = datetime.date.today()

print("Today's Date :", today)

now = datetime.datetime.now()

print("Current Date & Time :", now)

# ==========================================================
# DATE COMPONENTS
# ==========================================================

print("\n" + "=" * 70)
print("9. DATE COMPONENTS")
print("=" * 70)

print("Year  :", now.year)
print("Month :", now.month)
print("Day   :", now.day)

# ==========================================================
# TIME COMPONENTS
# ==========================================================

print("\n" + "=" * 70)
print("10. TIME COMPONENTS")
print("=" * 70)

print("Hour        :", now.hour)
print("Minute      :", now.minute)
print("Second      :", now.second)
print("Microsecond :", now.microsecond)

# ==========================================================
# DATE FORMATTING
# ==========================================================

print("\n" + "=" * 70)
print("11. DATE FORMATTING")
print("=" * 70)

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A"))
print(now.strftime("%B"))
print(now.strftime("%I:%M:%S %p"))

# ==========================================================
# CREATE CUSTOM DATE
# ==========================================================

print("\n" + "=" * 70)
print("12. CUSTOM DATE")
print("=" * 70)

birthday = datetime.date(2004, 3, 16)

print("Birthday :", birthday)

# ==========================================================
# DATE DIFFERENCE
# ==========================================================

print("\n" + "=" * 70)
print("13. DATE DIFFERENCE")
print("=" * 70)

difference = today - birthday

print("Days Since Birthday :", difference.days)

# ==========================================================
# TIMESPAN USING timedelta
# ==========================================================

print("\n" + "=" * 70)
print("14. timedelta")
print("=" * 70)

future = today + datetime.timedelta(days=30)

past = today - datetime.timedelta(days=30)

print("30 Days Later  :", future)
print("30 Days Before :", past)

# ==========================================================
# REAL-LIFE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("15. MINI BILLING SYSTEM")
print("=" * 70)

price = 2499.99

discount = random.randint(5, 20)

discount_amount = price * discount / 100

final_price = price - discount_amount

print("Product Price :", price)
print("Discount      :", discount, "%")
print("Final Price   :", round(final_price, 2))
print("Generated On  :", now.strftime("%d-%m-%Y %I:%M:%S %p"))

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to import modules.")
print("❌ Using random.randint() with wrong range.")
print("❌ Confusing ceil() and floor().")
print("❌ Forgetting parentheses while calling functions.")
print("❌ Naming your file math.py or random.py.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ math module performs mathematical calculations.")
print("✔ random module generates random values.")
print("✔ datetime module works with dates and time.")
print("✔ math provides sqrt(), factorial(), ceil(), floor(), gcd(), etc.")
print("✔ random provides randint(), choice(), sample(), shuffle(), etc.")
print("✔ datetime provides date, time, formatting, and timedelta.")
print("✔ These modules are widely used in real-world Python projects.")

print("=" * 70)
print("End of math_random_datetime.py")
print("=" * 70)
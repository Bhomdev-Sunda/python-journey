# ==========================================================
#        Introduction to Generators in Python - Day 18
# ==========================================================

print("=" * 70)
print("          INTRODUCTION TO GENERATORS IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS A GENERATOR?
# ==========================================================

"""
A Generator is a special type of function that produces
values one at a time instead of returning all values at once.

Generators use the 'yield' keyword instead of 'return'.

A generator remembers its state between function calls,
making it memory efficient.
"""

print("\nWHAT IS A GENERATOR?")
print("-" * 70)

print("A generator is a special function that")
print("produces one value at a time using the 'yield' keyword.")

# ==========================================================
# WHY DO WE USE GENERATORS?
# ==========================================================

print("\n" + "=" * 70)
print("WHY DO WE USE GENERATORS?")
print("=" * 70)

advantages = [
    "Memory Efficient",
    "Lazy Evaluation",
    "Works with Large Data",
    "Produces Values On Demand",
    "Faster for Huge Datasets",
    "Easy to Read",
    "Useful in Data Pipelines",
    "Ideal for Streaming Data"
]

for item in advantages:
    print("✔", item)

# ==========================================================
# SIMPLE GENERATOR
# ==========================================================

print("\n" + "=" * 70)
print("1. SIMPLE GENERATOR")
print("=" * 70)


def numbers():

    yield 10
    yield 20
    yield 30
    yield 40


generator = numbers()

print(generator)

# ==========================================================
# USING next()
# ==========================================================

print("\n" + "=" * 70)
print("2. USING next()")
print("=" * 70)

generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# ==========================================================
# StopIteration
# ==========================================================

print("\n" + "=" * 70)
print("3. StopIteration")
print("=" * 70)

generator = numbers()

try:

    while True:

        print(next(generator))

except StopIteration:

    print("Generator Finished.")

# ==========================================================
# USING for LOOP
# ==========================================================

print("\n" + "=" * 70)
print("4. USING for LOOP")
print("=" * 70)

for value in numbers():

    print(value)

# ==========================================================
# GENERATOR WITH LOOP
# ==========================================================

print("\n" + "=" * 70)
print("5. GENERATOR WITH LOOP")
print("=" * 70)


def count(limit):

    for number in range(1, limit + 1):

        yield number


for value in count(5):

    print(value)

# ==========================================================
# SQUARE GENERATOR
# ==========================================================

print("\n" + "=" * 70)
print("6. SQUARE GENERATOR")
print("=" * 70)


def squares(limit):

    for number in range(1, limit + 1):

        yield number ** 2


for square in squares(10):

    print(square)

# ==========================================================
# EVEN NUMBER GENERATOR
# ==========================================================

print("\n" + "=" * 70)
print("7. EVEN NUMBER GENERATOR")
print("=" * 70)


def even_numbers(limit):

    for number in range(2, limit + 1, 2):

        yield number


for number in even_numbers(20):

    print(number)

# ==========================================================
# ODD NUMBER GENERATOR
# ==========================================================

print("\n" + "=" * 70)
print("8. ODD NUMBER GENERATOR")
print("=" * 70)


def odd_numbers(limit):

    for number in range(1, limit + 1, 2):

        yield number


for number in odd_numbers(15):

    print(number)

# ==========================================================
# STRING GENERATOR
# ==========================================================

print("\n" + "=" * 70)
print("9. STRING GENERATOR")
print("=" * 70)


def letters(word):

    for character in word:

        yield character


for character in letters("PYTHON"):

    print(character)

# ==========================================================
# FIBONACCI GENERATOR
# ==========================================================

print("\n" + "=" * 70)
print("10. FIBONACCI GENERATOR")
print("=" * 70)


def fibonacci(limit):

    a = 0
    b = 1

    for _ in range(limit):

        yield a

        a, b = b, a + b


for number in fibonacci(10):

    print(number)

# ==========================================================
# GENERATOR OBJECT
# ==========================================================

print("\n" + "=" * 70)
print("11. GENERATOR OBJECT")
print("=" * 70)

generator = squares(5)

print(generator)

print(type(generator))

# ==========================================================
# MEMORY EFFICIENCY
# ==========================================================

print("\n" + "=" * 70)
print("12. MEMORY EFFICIENCY")
print("=" * 70)

large_generator = count(1_000_000)

print(next(large_generator))
print(next(large_generator))
print(next(large_generator))
print(next(large_generator))
print(next(large_generator))

print("Only required values are generated.")

# ==========================================================
# GENERATOR IS AN ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("13. GENERATOR IS AN ITERATOR")
print("=" * 70)

generator = numbers()

print(iter(generator) is generator)

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Reading Large Files",

    "Machine Learning",

    "Data Science",

    "API Responses",

    "Web Scraping",

    "Streaming Videos",

    "Processing CSV Files",

    "Database Records",

    "Sensor Data",

    "Log Processing"

]

for app in applications:

    print("✔", app)

# ==========================================================
# ADVANTAGES
# ==========================================================

print("\n" + "=" * 70)
print("ADVANTAGES")
print("=" * 70)

advantages = [

    "Consumes Less Memory",

    "Lazy Evaluation",

    "Produces Values On Demand",

    "Easy to Implement",

    "Ideal for Large Data",

    "Improves Performance"

]

for item in advantages:

    print("✔", item)

# ==========================================================
# LIMITATIONS
# ==========================================================

print("\n" + "=" * 70)
print("LIMITATIONS")
print("=" * 70)

limitations = [

    "Can Be Iterated Only Once",

    "No Random Access",

    "Cannot Use Indexing",

    "Values Are Not Stored"

]

for item in limitations:

    print("❌", item)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Using return instead of yield.")
print("❌ Reusing an exhausted generator.")
print("❌ Expecting indexing support.")
print("❌ Forgetting StopIteration with next().")
print("❌ Converting generators to lists unnecessarily.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use generators for large datasets.")
print("✔ Use yield instead of return when producing multiple values.")
print("✔ Prefer for-loops over repeated next() calls.")
print("✔ Convert to list only when necessary.")
print("✔ Use generators for streaming data.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Generators use the 'yield' keyword.")
print("✔ They produce one value at a time.")
print("✔ Generators are memory efficient.")
print("✔ A generator is also an iterator.")
print("✔ next() retrieves the next generated value.")
print("✔ Generators are ideal for processing large datasets.")

print("=" * 70)
print("End of 01_generators_intro.py")
print("=" * 70)
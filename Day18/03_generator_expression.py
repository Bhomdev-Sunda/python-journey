# ==========================================================
#      Generator Expressions in Python - Day 18
# ==========================================================

print("=" * 70)
print("         GENERATOR EXPRESSIONS IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS A GENERATOR EXPRESSION?
# ==========================================================

"""
A Generator Expression is a compact way of creating
a generator.

It looks similar to a list comprehension,
but uses parentheses () instead of square brackets [].

List Comprehension:
[x for x in iterable]

Generator Expression:
(x for x in iterable)
"""

print("\nWHAT IS A GENERATOR EXPRESSION?")
print("-" * 70)

print("A generator expression creates")
print("values one at a time.")
print("It uses parentheses ().")

# ==========================================================
# WHY USE GENERATOR EXPRESSIONS?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE GENERATOR EXPRESSIONS?")
print("=" * 70)

advantages = [

    "Memory Efficient",

    "Lazy Evaluation",

    "Simple Syntax",

    "Fast for Large Data",

    "Easy to Read",

    "Creates Generator Objects"

]

for item in advantages:

    print("✔", item)

# ==========================================================
# SIMPLE GENERATOR EXPRESSION
# ==========================================================

print("\n" + "=" * 70)
print("1. SIMPLE GENERATOR EXPRESSION")
print("=" * 70)

numbers = (number for number in range(1, 6))

print(numbers)

# ==========================================================
# USING next()
# ==========================================================

print("\n" + "=" * 70)
print("2. USING next()")
print("=" * 70)

numbers = (number for number in range(1, 6))

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

# ==========================================================
# USING for LOOP
# ==========================================================

print("\n" + "=" * 70)
print("3. USING for LOOP")
print("=" * 70)

numbers = (number for number in range(1, 6))

for number in numbers:

    print(number)

# ==========================================================
# SQUARE NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("4. SQUARE NUMBERS")
print("=" * 70)

squares = (number ** 2 for number in range(1, 11))

for square in squares:

    print(square)

# ==========================================================
# EVEN NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("5. EVEN NUMBERS")
print("=" * 70)

evens = (number for number in range(1, 21) if number % 2 == 0)

for number in evens:

    print(number)

# ==========================================================
# ODD NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("6. ODD NUMBERS")
print("=" * 70)

odds = (number for number in range(1, 21) if number % 2 != 0)

for number in odds:

    print(number)

# ==========================================================
# STRING EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("7. STRING EXAMPLE")
print("=" * 70)

letters = (character for character in "PYTHON")

for letter in letters:

    print(letter)

# ==========================================================
# LIST vs GENERATOR
# ==========================================================

print("\n" + "=" * 70)
print("8. LIST vs GENERATOR")
print("=" * 70)

list_data = [number for number in range(10)]

generator_data = (number for number in range(10))

print("List      :", list_data)

print("Generator :", generator_data)

# ==========================================================
# TYPE COMPARISON
# ==========================================================

print("\n" + "=" * 70)
print("9. TYPE COMPARISON")
print("=" * 70)

print(type(list_data))

print(type(generator_data))

# ==========================================================
# MEMORY EFFICIENCY
# ==========================================================

print("\n" + "=" * 70)
print("10. MEMORY EFFICIENCY")
print("=" * 70)

large_generator = (number for number in range(1, 1000001))

print(next(large_generator))
print(next(large_generator))
print(next(large_generator))
print(next(large_generator))
print(next(large_generator))

print("Generator creates values only when required.")

# ==========================================================
# SUM OF VALUES
# ==========================================================

print("\n" + "=" * 70)
print("11. SUM USING GENERATOR")
print("=" * 70)

result = sum(number for number in range(1, 101))

print("Sum =", result)

# ==========================================================
# MAXIMUM VALUE
# ==========================================================

print("\n" + "=" * 70)
print("12. MAXIMUM VALUE")
print("=" * 70)

largest = max(number for number in range(50))

print(largest)

# ==========================================================
# MINIMUM VALUE
# ==========================================================

print("\n" + "=" * 70)
print("13. MINIMUM VALUE")
print("=" * 70)

smallest = min(number for number in range(50))

print(smallest)

# ==========================================================
# FILTERING DATA
# ==========================================================

print("\n" + "=" * 70)
print("14. FILTERING DATA")
print("=" * 70)

numbers = (number for number in range(1, 31) if number % 3 == 0)

for number in numbers:

    print(number)

# ==========================================================
# NESTED GENERATOR EXPRESSION
# ==========================================================

print("\n" + "=" * 70)
print("15. NESTED GENERATOR")
print("=" * 70)

pairs = ((x, y) for x in range(1, 4) for y in range(1, 3))

for pair in pairs:

    print(pair)

# ==========================================================
# GENERATOR EXHAUSTION
# ==========================================================

print("\n" + "=" * 70)
print("16. GENERATOR EXHAUSTION")
print("=" * 70)

generator = (number for number in range(3))

for number in generator:

    print(number)

print("Generator Finished")

print(list(generator))

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Reading Large Files",

    "Machine Learning",

    "Web Scraping",

    "Streaming Data",

    "Database Queries",

    "CSV Processing",

    "API Responses",

    "Big Data Analysis"

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

    "Produces Data On Demand",

    "Cleaner Syntax",

    "Better Performance",

    "Ideal for Huge Data"

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

    "No Indexing",

    "No Random Access",

    "Values Are Not Stored"

]

for item in limitations:

    print("❌", item)

# ==========================================================
# LIST COMPREHENSION vs GENERATOR EXPRESSION
# ==========================================================

print("\n" + "=" * 70)
print("LIST COMPREHENSION vs GENERATOR EXPRESSION")
print("=" * 70)

print(f"{'LIST COMPREHENSION':<30} {'GENERATOR EXPRESSION'}")
print("-" * 65)

comparison = [

    ("Uses []", "Uses ()"),

    ("Creates List", "Creates Generator"),

    ("Higher Memory", "Lower Memory"),

    ("Immediate Evaluation", "Lazy Evaluation"),

    ("Supports Indexing", "No Indexing"),

    ("Reusable", "Single Use")

]

for left, right in comparison:

    print(f"{left:<30} {right}")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Expecting indexing support.")
print("❌ Reusing exhausted generators.")
print("❌ Forgetting parentheses ().")
print("❌ Converting generators to lists unnecessarily.")
print("❌ Confusing list comprehensions with generators.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use generator expressions for large datasets.")
print("✔ Prefer list comprehensions for small collections.")
print("✔ Use generators when values are needed one by one.")
print("✔ Avoid converting generators into lists unless necessary.")
print("✔ Use built-in functions like sum(), max(), min() directly.")

# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

questions = [

    "What is a generator expression?",

    "Difference between list comprehension and generator expression?",

    "Why are generator expressions memory efficient?",

    "Can a generator expression be reused?",

    "Which brackets are used in generator expressions?",

    "Can next() be used on generator expressions?",

    "When should generator expressions be preferred?",

    "Do generator expressions support indexing?"

]

for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Generator expressions use parentheses ().")
print("✔ They create generator objects.")
print("✔ Values are produced lazily.")
print("✔ They consume less memory than lists.")
print("✔ They are excellent for processing large datasets.")
print("✔ Generator expressions are exhausted after one complete iteration.")

print("=" * 70)
print("End of 03_generator_expression.py")
print("=" * 70)
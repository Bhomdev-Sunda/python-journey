# ==========================================================
#         Day 18 Practice - Python Generators
# ==========================================================

"""
Topics Covered
--------------
1. Generator Functions
2. yield
3. return vs yield
4. next()
5. Generator Expressions
6. Infinite Generators
7. Fibonacci Generator
8. Countdown Generator
9. Prime Number Generator
10. Generator Pipeline
"""

print("=" * 75)
print("          DAY 18 PRACTICE - PYTHON GENERATORS")
print("=" * 75)

# ==========================================================
# QUESTION 1
# SIMPLE GENERATOR
# ==========================================================

print("\n1. SIMPLE GENERATOR")
print("-" * 75)


def numbers():

    yield 10
    yield 20
    yield 30
    yield 40


gen = numbers()

for value in gen:

    print(value)

# ==========================================================
# QUESTION 2
# USING next()
# ==========================================================

print("\n2. USING next()")
print("-" * 75)

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

try:

    print(next(gen))

except StopIteration:

    print("Generator Finished")

# ==========================================================
# QUESTION 3
# COUNT GENERATOR
# ==========================================================

print("\n3. COUNT GENERATOR")
print("-" * 75)


def counter(limit):

    for number in range(1, limit + 1):

        yield number


for value in counter(10):

    print(value)

# ==========================================================
# QUESTION 4
# SQUARE GENERATOR
# ==========================================================

print("\n4. SQUARE GENERATOR")
print("-" * 75)


def squares(limit):

    for number in range(1, limit + 1):

        yield number ** 2


for value in squares(10):

    print(value)

# ==========================================================
# QUESTION 5
# EVEN NUMBER GENERATOR
# ==========================================================

print("\n5. EVEN NUMBER GENERATOR")
print("-" * 75)


def even_numbers(limit):

    for number in range(2, limit + 1, 2):

        yield number


for value in even_numbers(20):

    print(value)

# ==========================================================
# QUESTION 6
# ODD NUMBER GENERATOR
# ==========================================================

print("\n6. ODD NUMBER GENERATOR")
print("-" * 75)


def odd_numbers(limit):

    for number in range(1, limit + 1, 2):

        yield number


for value in odd_numbers(15):

    print(value)

# ==========================================================
# QUESTION 7
# FIBONACCI GENERATOR
# ==========================================================

print("\n7. FIBONACCI GENERATOR")
print("-" * 75)


def fibonacci(limit):

    a = 0
    b = 1

    for _ in range(limit):

        yield a

        a, b = b, a + b


for number in fibonacci(12):

    print(number)

# ==========================================================
# QUESTION 8
# COUNTDOWN GENERATOR
# ==========================================================

print("\n8. COUNTDOWN GENERATOR")
print("-" * 75)


def countdown(start):

    while start > 0:

        yield start

        start -= 1


for number in countdown(10):

    print(number)

# ==========================================================
# QUESTION 9
# GENERATOR EXPRESSION
# ==========================================================

print("\n9. GENERATOR EXPRESSION")
print("-" * 75)

generator = (number ** 2 for number in range(1, 11))

for value in generator:

    print(value)

# ==========================================================
# QUESTION 10
# FILTERED GENERATOR
# ==========================================================

print("\n10. FILTERED GENERATOR")
print("-" * 75)

generator = (

    number

    for number in range(1, 31)

    if number % 3 == 0

)

for value in generator:

    print(value)

# ==========================================================
# QUESTION 11
# INFINITE COUNTER
# ==========================================================

print("\n11. INFINITE COUNTER")
print("-" * 75)


def infinite_counter():

    number = 1

    while True:

        yield number

        number += 1


gen = infinite_counter()

for _ in range(10):

    print(next(gen))

# ==========================================================
# QUESTION 12
# INFINITE FIBONACCI
# ==========================================================

print("\n12. INFINITE FIBONACCI")
print("-" * 75)


def infinite_fibonacci():

    a = 0
    b = 1

    while True:

        yield a

        a, b = b, a + b


gen = infinite_fibonacci()

for _ in range(15):

    print(next(gen))

# ==========================================================
# QUESTION 13
# PRIME NUMBER GENERATOR
# ==========================================================

print("\n13. PRIME NUMBER GENERATOR")
print("-" * 75)


def prime_generator(limit):

    for number in range(2, limit + 1):

        is_prime = True

        for divisor in range(2, int(number ** 0.5) + 1):

            if number % divisor == 0:

                is_prime = False

                break

        if is_prime:

            yield number


for prime in prime_generator(50):

    print(prime)

# ==========================================================
# QUESTION 14
# CHARACTER GENERATOR
# ==========================================================

print("\n14. CHARACTER GENERATOR")
print("-" * 75)


def characters(text):

    for character in text:

        yield character


for char in characters("PYTHON"):

    print(char)

# ==========================================================
# QUESTION 15
# GENERATOR PIPELINE
# ==========================================================

print("\n15. GENERATOR PIPELINE")
print("-" * 75)


def numbers():

    for number in range(1, 11):

        yield number


def square(data):

    for value in data:

        yield value ** 2


def even(data):

    for value in data:

        if value % 2 == 0:

            yield value


pipeline = even(square(numbers()))

for value in pipeline:

    print(value)

# ==========================================================
# QUESTION 16
# SUM USING GENERATOR
# ==========================================================

print("\n16. SUM USING GENERATOR")
print("-" * 75)

total = sum(number for number in range(1, 101))

print(total)

# ==========================================================
# QUESTION 17
# MAXIMUM VALUE
# ==========================================================

print("\n17. MAXIMUM VALUE")
print("-" * 75)

largest = max(number for number in range(1, 500))

print(largest)

# ==========================================================
# QUESTION 18
# MINIMUM VALUE
# ==========================================================

print("\n18. MINIMUM VALUE")
print("-" * 75)

smallest = min(number for number in range(1, 500))

print(smallest)

# ==========================================================
# QUESTION 19
# RETURN vs YIELD
# ==========================================================

print("\n19. RETURN vs YIELD")
print("-" * 75)


def return_example():

    return [1, 2, 3, 4, 5]


def yield_example():

    for number in range(1, 6):

        yield number


print(return_example())

for value in yield_example():

    print(value)

# ==========================================================
# QUESTION 20
# INTERVIEW REVISION
# ==========================================================

print("\n20. INTERVIEW QUESTIONS")
print("-" * 75)

questions = [

    "What is a generator?",

    "Why are generators memory efficient?",

    "Difference between yield and return?",

    "What is lazy evaluation?",

    "What is a generator expression?",

    "Difference between list comprehension and generator expression?",

    "What is an infinite generator?",

    "How do generators improve performance?",

    "Can generators be reused?",

    "What exception ends a generator?"

]

for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")

# ==========================================================
# KEY TAKEAWAYS
# ==========================================================

print("\n21. KEY TAKEAWAYS")
print("-" * 75)

points = [

    "Generators use the yield keyword.",

    "Generators produce one value at a time.",

    "Generators save memory.",

    "yield pauses execution.",

    "return ends execution.",

    "Generator expressions use ().",

    "Infinite generators usually use while True.",

    "next() gets the next generated value.",

    "Generators support lazy evaluation.",

    "Ideal for processing huge datasets."

]

for point in points:

    print("✔", point)

print("\n" + "=" * 75)
print("          DAY 18 PRACTICE COMPLETED SUCCESSFULLY")
print("=" * 75)
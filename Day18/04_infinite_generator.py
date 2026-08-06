# ==========================================================
#        Infinite Generators in Python - Day 18
# ==========================================================

print("=" * 70)
print("          INFINITE GENERATORS IN PYTHON")
print("=" * 70)

"""
Infinite Generators
-------------------

An infinite generator never stops producing values.

Instead of ending after a fixed number of iterations,
it keeps generating values forever until we stop it.

Infinite generators are useful for:

✔ Live Data Streams
✔ Sensor Readings
✔ Server Logs
✔ Game Loops
✔ Infinite Counters
✔ Machine Learning Pipelines
✔ Random Data Generation
"""

# ==========================================================
# WHAT IS AN INFINITE GENERATOR?
# ==========================================================

print("\nWHAT IS AN INFINITE GENERATOR?")
print("-" * 70)

print("An infinite generator continuously generates")
print("values without reaching StopIteration.")
print("Usually created using a while True loop.")

# ==========================================================
# EXAMPLE 1
# INFINITE COUNTER
# ==========================================================

print("\n" + "=" * 70)
print("1. INFINITE COUNTER")
print("=" * 70)


def counter():

    number = 1

    while True:

        yield number

        number += 1


gen = counter()

for _ in range(10):

    print(next(gen))

# ==========================================================
# EXAMPLE 2
# INFINITE EVEN NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("2. INFINITE EVEN NUMBERS")
print("=" * 70)


def even_numbers():

    number = 2

    while True:

        yield number

        number += 2


gen = even_numbers()

for _ in range(10):

    print(next(gen))

# ==========================================================
# EXAMPLE 3
# INFINITE ODD NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("3. INFINITE ODD NUMBERS")
print("=" * 70)


def odd_numbers():

    number = 1

    while True:

        yield number

        number += 2


gen = odd_numbers()

for _ in range(10):

    print(next(gen))

# ==========================================================
# EXAMPLE 4
# INFINITE SQUARES
# ==========================================================

print("\n" + "=" * 70)
print("4. INFINITE SQUARE NUMBERS")
print("=" * 70)


def squares():

    number = 1

    while True:

        yield number ** 2

        number += 1


gen = squares()

for _ in range(10):

    print(next(gen))

# ==========================================================
# EXAMPLE 5
# INFINITE FIBONACCI
# ==========================================================

print("\n" + "=" * 70)
print("5. INFINITE FIBONACCI")
print("=" * 70)


def fibonacci():

    a = 0
    b = 1

    while True:

        yield a

        a, b = b, a + b


gen = fibonacci()

for _ in range(15):

    print(next(gen))

# ==========================================================
# EXAMPLE 6
# ALPHABET CYCLE
# ==========================================================

print("\n" + "=" * 70)
print("6. ALPHABET CYCLE")
print("=" * 70)


def alphabet():

    while True:

        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

            yield letter


gen = alphabet()

for _ in range(30):

    print(next(gen), end=" ")

print()

# ==========================================================
# EXAMPLE 7
# TRAFFIC LIGHT SIMULATION
# ==========================================================

print("\n" + "=" * 70)
print("7. TRAFFIC LIGHT SIMULATION")
print("=" * 70)


def traffic_light():

    lights = ["🔴 RED", "🟡 YELLOW", "🟢 GREEN"]

    while True:

        for light in lights:

            yield light


gen = traffic_light()

for _ in range(9):

    print(next(gen))

# ==========================================================
# EXAMPLE 8
# DAYS OF WEEK
# ==========================================================

print("\n" + "=" * 70)
print("8. DAYS OF WEEK")
print("=" * 70)


def week_days():

    days = [

        "Monday",

        "Tuesday",

        "Wednesday",

        "Thursday",

        "Friday",

        "Saturday",

        "Sunday"

    ]

    while True:

        for day in days:

            yield day


gen = week_days()

for _ in range(12):

    print(next(gen))

# ==========================================================
# EXAMPLE 9
# RANDOM NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("9. RANDOM NUMBER GENERATOR")
print("=" * 70)

import random


def random_numbers():

    while True:

        yield random.randint(1, 100)


gen = random_numbers()

for _ in range(10):

    print(next(gen))

# ==========================================================
# EXAMPLE 10
# COUNTDOWN (FINITE)
# ==========================================================

print("\n" + "=" * 70)
print("10. FINITE COUNTDOWN")
print("=" * 70)


def countdown(start):

    while start > 0:

        yield start

        start -= 1


for number in countdown(10):

    print(number)

# ==========================================================
# MANUAL CONTROL
# ==========================================================

print("\n" + "=" * 70)
print("11. MANUAL CONTROL USING next()")
print("=" * 70)

gen = counter()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# ==========================================================
# WHY INFINITE GENERATORS?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE INFINITE GENERATORS?")
print("=" * 70)

advantages = [

    "No Memory Waste",

    "Unlimited Data",

    "Streaming Support",

    "Real-Time Processing",

    "Lazy Evaluation",

    "Simple Implementation"

]

for item in advantages:

    print("✔", item)

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Live Sensor Data",

    "Weather Monitoring",

    "Server Logs",

    "Stock Prices",

    "Game Engines",

    "Chat Servers",

    "Machine Learning",

    "WebSocket Streams",

    "IoT Devices",

    "GPS Tracking"

]

for app in applications:

    print("✔", app)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Using 'for' directly on an infinite generator.")
print("❌ Forgetting to limit iteration.")
print("❌ Creating accidental infinite loops.")
print("❌ Converting infinite generators to list().")
print("❌ Not using next() carefully.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Control infinite generators using next().")
print("✔ Limit output with range().")
print("✔ Never convert them to a list.")
print("✔ Keep generator logic simple.")
print("✔ Use them for streaming data.")

# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

questions = [

    "What is an infinite generator?",

    "How is it created?",

    "Why do we use while True?",

    "Can an infinite generator end?",

    "How do we safely use an infinite generator?",

    "Can next() be used with infinite generators?",

    "Why shouldn't you convert an infinite generator to a list?",

    "Give one real-world use of infinite generators."

]

for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Infinite generators never stop automatically.")
print("✔ They commonly use 'while True'.")
print("✔ Values are generated only when requested.")
print("✔ They are extremely memory efficient.")
print("✔ Always limit iteration using next() or range().")
print("✔ Never convert an infinite generator into a list.")

print("=" * 70)
print("End of 04_infinite_generator.py")
print("=" * 70)
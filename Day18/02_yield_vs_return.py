# ==========================================================
#          yield vs return in Python - Day 18
# ==========================================================

print("=" * 70)
print("              yield vs return IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS return?
# ==========================================================

"""
return
------

1. Ends the function immediately.
2. Returns a single value (or object).
3. Function execution stops.
4. Cannot resume execution.
"""

print("\nWHAT IS return?")
print("-" * 70)

print("return immediately exits the function.")
print("After return executes, the function finishes.")

# ==========================================================
# SIMPLE return EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("1. SIMPLE return EXAMPLE")
print("=" * 70)


def add(a, b):

    return a + b


result = add(10, 20)

print("Result :", result)

# ==========================================================
# return STOPS EXECUTION
# ==========================================================

print("\n" + "=" * 70)
print("2. return STOPS EXECUTION")
print("=" * 70)


def example():

    print("Start")

    return

    print("This will never execute")


example()

# ==========================================================
# WHAT IS yield?
# ==========================================================

print("\n" + "=" * 70)
print("WHAT IS yield?")
print("=" * 70)

"""
yield

1. Pauses the function.
2. Returns one value.
3. Remembers function state.
4. Continues from where it stopped.
5. Creates a generator object.
"""

print("yield pauses the function instead of ending it.")
print("The function resumes from the same position.")

# ==========================================================
# SIMPLE yield EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("3. SIMPLE yield EXAMPLE")
print("=" * 70)


def numbers():

    yield 10

    yield 20

    yield 30


generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))

# ==========================================================
# yield REMEMBERS STATE
# ==========================================================

print("\n" + "=" * 70)
print("4. yield REMEMBERS STATE")
print("=" * 70)


def demo():

    print("Before First Yield")

    yield 1

    print("Before Second Yield")

    yield 2

    print("Before Third Yield")

    yield 3

    print("Generator Finished")


generator = demo()

print(next(generator))
print(next(generator))
print(next(generator))

try:

    print(next(generator))

except StopIteration:

    print("No More Values")

# ==========================================================
# MULTIPLE return
# ==========================================================

print("\n" + "=" * 70)
print("5. MULTIPLE return")
print("=" * 70)


def get_square(number):

    return number ** 2


print(get_square(5))
print(get_square(10))

# ==========================================================
# MULTIPLE yield
# ==========================================================

print("\n" + "=" * 70)
print("6. MULTIPLE yield")
print("=" * 70)


def squares(limit):

    for number in range(1, limit + 1):

        yield number ** 2


for square in squares(5):

    print(square)

# ==========================================================
# return RETURNS LIST
# ==========================================================

print("\n" + "=" * 70)
print("7. return RETURNS ENTIRE LIST")
print("=" * 70)


def get_numbers():

    numbers = []

    for number in range(1, 6):

        numbers.append(number)

    return numbers


print(get_numbers())

# ==========================================================
# yield RETURNS ONE VALUE
# ==========================================================

print("\n" + "=" * 70)
print("8. yield RETURNS ONE VALUE")
print("=" * 70)


def generate_numbers():

    for number in range(1, 6):

        yield number


for value in generate_numbers():

    print(value)

# ==========================================================
# MEMORY COMPARISON
# ==========================================================

print("\n" + "=" * 70)
print("9. MEMORY COMPARISON")
print("=" * 70)


def list_function():

    return list(range(1, 1000001))


def generator_function():

    for number in range(1, 1000001):

        yield number


generator = generator_function()

print(next(generator))
print(next(generator))
print(next(generator))

print("Generator creates values only when needed.")

# ==========================================================
# TYPE COMPARISON
# ==========================================================

print("\n" + "=" * 70)
print("10. TYPE COMPARISON")
print("=" * 70)

print(type(get_numbers()))

print(type(generate_numbers()))

# ==========================================================
# yield INSIDE LOOP
# ==========================================================

print("\n" + "=" * 70)
print("11. yield INSIDE LOOP")
print("=" * 70)


def countdown(start):

    while start > 0:

        yield start

        start -= 1


for number in countdown(5):

    print(number)

# ==========================================================
# return INSIDE LOOP
# ==========================================================

print("\n" + "=" * 70)
print("12. return INSIDE LOOP")
print("=" * 70)


def first_even():

    for number in range(1, 20):

        if number % 2 == 0:

            return number


print(first_even())

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Reading Huge Files",

    "API Pagination",

    "Streaming Videos",

    "Machine Learning",

    "Big Data",

    "Database Queries",

    "Sensor Data",

    "Log Processing"

]

for app in applications:

    print("✔", app)

# ==========================================================
# yield vs return TABLE
# ==========================================================

print("\n" + "=" * 70)
print("yield vs return")
print("=" * 70)

print(f"{'return':<20} {'yield':<25}")
print("-" * 45)

comparison = [

    ("Ends Function", "Pauses Function"),

    ("Returns One Object", "Returns One Value"),

    ("No State Saved", "State Preserved"),

    ("Not Lazy", "Lazy Evaluation"),

    ("Returns List/Object", "Returns Generator"),

    ("Higher Memory", "Lower Memory"),

    ("Runs Once", "Resumes Execution")

]

for left, right in comparison:

    print(f"{left:<20} {right:<25}")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Using return when yield is required.")
print("❌ Expecting generators to support indexing.")
print("❌ Reusing exhausted generators.")
print("❌ Forgetting next() or for-loop.")
print("❌ Converting generators into lists unnecessarily.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use return for final results.")
print("✔ Use yield for sequences.")
print("✔ Use generators for large datasets.")
print("✔ Prefer for-loops over repeated next().")
print("✔ Keep generator logic simple.")

# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

questions = [

    "What is yield?",

    "What is return?",

    "Difference between yield and return?",

    "Why are generators memory efficient?",

    "Does yield stop a function?",

    "Can a generator have multiple yield statements?",

    "Can return and yield exist in the same function?",

    "When should you use yield instead of return?"

]

for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ return ends a function immediately.")
print("✔ yield pauses a function and resumes later.")
print("✔ yield creates a generator object.")
print("✔ Generators are memory efficient.")
print("✔ yield supports lazy evaluation.")
print("✔ Use return for final results and yield for sequences.")

print("=" * 70)
print("End of 02_yield_vs_return.py")
print("=" * 70)
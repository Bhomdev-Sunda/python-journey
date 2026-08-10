# ==========================================================
#            Decorators in Python - Day 19
# ==========================================================

print("=" * 70)
print("               DECORATORS IN PYTHON")
print("=" * 70)

"""
A decorator is a function that modifies or extends
the behavior of another function without changing
its original source code.

Decorators are built using:
1. First-Class Functions
2. Nested Functions
3. Closures
"""

# ==========================================================
# WHAT IS A DECORATOR?
# ==========================================================

print("\nWHAT IS A DECORATOR?")
print("-" * 70)

print("A decorator wraps another function")
print("to add extra functionality.")

# ==========================================================
# EXAMPLE 1
# BASIC DECORATOR
# ==========================================================

print("\n" + "=" * 70)
print("1. BASIC DECORATOR")
print("=" * 70)


def decorator(function):

    def wrapper():

        print("Before Function")

        function()

        print("After Function")

    return wrapper


@decorator
def greet():

    print("Hello Python")


greet()

# ==========================================================
# EXAMPLE 2
# DECORATOR WITHOUT @ SYMBOL
# ==========================================================

print("\n" + "=" * 70)
print("2. WITHOUT @ DECORATOR")
print("=" * 70)


def hello():

    print("Hello World")


decorated = decorator(hello)

decorated()

# ==========================================================
# EXAMPLE 3
# DECORATOR WITH PARAMETERS
# ==========================================================

print("\n" + "=" * 70)
print("3. DECORATOR WITH PARAMETERS")
print("=" * 70)


def smart_decorator(function):

    def wrapper(name):

        print("Starting Function")

        function(name)

        print("Function Finished")

    return wrapper


@smart_decorator
def welcome(name):

    print(f"Welcome {name}")


welcome("Bhomdev")

# ==========================================================
# EXAMPLE 4
# *args AND **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("4. *args AND **kwargs")
print("=" * 70)


def universal_decorator(function):

    def wrapper(*args, **kwargs):

        print("Decorator Started")

        result = function(*args, **kwargs)

        print("Decorator Finished")

        return result

    return wrapper


@universal_decorator
def add(a, b):

    return a + b


print(add(10, 20))

# ==========================================================
# EXAMPLE 5
# LOGIN DECORATOR
# ==========================================================

print("\n" + "=" * 70)
print("5. LOGIN DECORATOR")
print("=" * 70)

logged_in = True


def login_required(function):

    def wrapper():

        if logged_in:

            function()

        else:

            print("Access Denied")

    return wrapper


@login_required
def dashboard():

    print("Welcome to Dashboard")


dashboard()

# ==========================================================
# EXAMPLE 6
# TIMER DECORATOR
# ==========================================================

print("\n" + "=" * 70)
print("6. TIMER DECORATOR")
print("=" * 70)

import time


def timer(function):

    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        print(f"Execution Time: {end - start:.6f} seconds")

        return result

    return wrapper


@timer
def calculate():

    total = 0

    for number in range(1_000_000):

        total += number

    return total


calculate()

# ==========================================================
# EXAMPLE 7
# LOGGING DECORATOR
# ==========================================================

print("\n" + "=" * 70)
print("7. LOGGING DECORATOR")
print("=" * 70)


def logger(function):

    def wrapper(*args, **kwargs):

        print(f"Calling {function.__name__}()")

        result = function(*args, **kwargs)

        print(f"{function.__name__}() Completed")

        return result

    return wrapper


@logger
def multiply(a, b):

    return a * b


print(multiply(5, 8))

# ==========================================================
# EXAMPLE 8
# AUTHORIZATION DECORATOR
# ==========================================================

print("\n" + "=" * 70)
print("8. AUTHORIZATION DECORATOR")
print("=" * 70)

role = "admin"


def admin_only(function):

    def wrapper():

        if role == "admin":

            function()

        else:

            print("Permission Denied")

    return wrapper


@admin_only
def delete_database():

    print("Database Deleted Successfully")


delete_database()

# ==========================================================
# EXAMPLE 9
# DECORATOR RETURNING VALUE
# ==========================================================

print("\n" + "=" * 70)
print("9. RETURN VALUE")
print("=" * 70)


def uppercase(function):

    def wrapper():

        return function().upper()

    return wrapper


@uppercase
def language():

    return "python"


print(language())

# ==========================================================
# EXAMPLE 10
# STACKING DECORATORS
# ==========================================================

print("\n" + "=" * 70)
print("10. STACKING DECORATORS")
print("=" * 70)


def star(function):

    def wrapper():

        print("*" * 30)

        function()

        print("*" * 30)

    return wrapper


def hash_line(function):

    def wrapper():

        print("#" * 30)

        function()

        print("#" * 30)

    return wrapper


@star
@hash_line
def message():

    print("Decorators are powerful!")


message()

# ==========================================================
# EXAMPLE 11
# DECORATOR WITH ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("11. DECORATOR FACTORY")
print("=" * 70)


def repeat(times):

    def decorator(function):

        def wrapper():

            for _ in range(times):

                function()

        return wrapper

    return decorator


@repeat(3)
def hello():

    print("Hello!")

hello()

# ==========================================================
# WHY DECORATORS?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE DECORATORS?")
print("=" * 70)

advantages = [

    "Reusable Code",

    "Code Separation",

    "Cleaner Functions",

    "Logging",

    "Authentication",

    "Caching",

    "Timing",

    "Validation"

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

    "FastAPI Routes",

    "Flask Routes",

    "Django Views",

    "Authentication",

    "Authorization",

    "Caching",

    "Performance Monitoring",

    "Logging",

    "Retry Mechanisms",

    "API Rate Limiting"

]

for app in applications:

    print("✔", app)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to return wrapper.")
print("❌ Forgetting to return function result.")
print("❌ Ignoring *args and **kwargs.")
print("❌ Calling function instead of passing it.")
print("❌ Losing metadata without functools.wraps.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use *args and **kwargs for flexibility.")
print("✔ Return the original function result.")
print("✔ Keep decorators focused on one task.")
print("✔ Use functools.wraps in production.")
print("✔ Use decorators to separate reusable logic.")

# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

questions = [

    "What is a decorator?",

    "Why do we use decorators?",

    "How are decorators implemented?",

    "What is a wrapper function?",

    "Why use *args and **kwargs in decorators?",

    "Can decorators return values?",

    "What are stacked decorators?",

    "Give real-world uses of decorators."

]

for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Decorators modify function behavior.")
print("✔ They are built using closures.")
print("✔ Wrapper functions add extra functionality.")
print("✔ Use *args and **kwargs for generic decorators.")
print("✔ Decorators are widely used in Flask, Django, and FastAPI.")

print("=" * 70)
print("End of 04_decorators.py")
print("=" * 70)
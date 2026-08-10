# ==========================================================
#            Closures in Python - Day 19
# ==========================================================

print("=" * 70)
print("                CLOSURES IN PYTHON")
print("=" * 70)

"""
A Closure is created when:

1. A function is defined inside another function.
2. The inner function uses variables from the outer function.
3. The outer function returns the inner function.
4. The inner function remembers the outer variables
   even after the outer function has finished.

Closures are one of the most important concepts
behind Python decorators.
"""

# ==========================================================
# WHAT IS A CLOSURE?
# ==========================================================

print("\nWHAT IS A CLOSURE?")
print("-" * 70)

print("A closure remembers variables")
print("from the outer function even")
print("after the outer function has ended.")

# ==========================================================
# EXAMPLE 1
# SIMPLE CLOSURE
# ==========================================================

print("\n" + "=" * 70)
print("1. SIMPLE CLOSURE")
print("=" * 70)


def outer():

    message = "Hello from Closure!"

    def inner():

        print(message)

    return inner


closure = outer()

closure()

# ==========================================================
# EXAMPLE 2
# CLOSURE WITH PARAMETERS
# ==========================================================

print("\n" + "=" * 70)
print("2. CLOSURE WITH PARAMETERS")
print("=" * 70)


def greet(name):

    def message():

        print(f"Welcome {name}")

    return message


user1 = greet("Bhomdev")
user2 = greet("Rahul")

user1()
user2()

# ==========================================================
# EXAMPLE 3
# MULTIPLIER CLOSURE
# ==========================================================

print("\n" + "=" * 70)
print("3. MULTIPLIER CLOSURE")
print("=" * 70)


def multiplier(number):

    def multiply(value):

        return value * number

    return multiply


double = multiplier(2)
triple = multiplier(3)
ten_times = multiplier(10)

print(double(10))
print(triple(10))
print(ten_times(10))

# ==========================================================
# EXAMPLE 4
# POWER FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("4. POWER FUNCTION")
print("=" * 70)


def power(exponent):

    def calculate(number):

        return number ** exponent

    return calculate


square = power(2)
cube = power(3)

print(square(5))
print(cube(5))

# ==========================================================
# EXAMPLE 5
# COUNTER USING nonlocal
# ==========================================================

print("\n" + "=" * 70)
print("5. COUNTER USING nonlocal")
print("=" * 70)


def counter():

    count = 0

    def increment():

        nonlocal count

        count += 1

        print("Count:", count)

    return increment


visit = counter()

visit()
visit()
visit()
visit()

# ==========================================================
# EXAMPLE 6
# BANK ACCOUNT
# ==========================================================

print("\n" + "=" * 70)
print("6. BANK ACCOUNT")
print("=" * 70)


def bank_account(balance):

    def deposit(amount):

        nonlocal balance

        balance += amount

        print("Current Balance:", balance)

    return deposit


account = bank_account(1000)

account(500)
account(250)
account(100)

# ==========================================================
# EXAMPLE 7
# LOGIN ATTEMPTS
# ==========================================================

print("\n" + "=" * 70)
print("7. LOGIN ATTEMPTS")
print("=" * 70)


def login_system():

    attempts = 0

    def login():

        nonlocal attempts

        attempts += 1

        print(f"Login Attempt {attempts}")

    return login


login = login_system()

login()
login()
login()

# ==========================================================
# EXAMPLE 8
# DISCOUNT CALCULATOR
# ==========================================================

print("\n" + "=" * 70)
print("8. DISCOUNT CALCULATOR")
print("=" * 70)


def discount(percent):

    def calculate(price):

        return price - (price * percent / 100)

    return calculate


ten_percent = discount(10)
twenty_percent = discount(20)

print(ten_percent(1000))
print(twenty_percent(1000))

# ==========================================================
# EXAMPLE 9
# MESSAGE GENERATOR
# ==========================================================

print("\n" + "=" * 70)
print("9. MESSAGE GENERATOR")
print("=" * 70)


def message_generator(prefix):

    def display(name):

        print(f"{prefix} {name}")

    return display


hello = message_generator("Hello")
welcome = message_generator("Welcome")

hello("Amit")
welcome("Priya")

# ==========================================================
# EXAMPLE 10
# AREA CALCULATOR
# ==========================================================

print("\n" + "=" * 70)
print("10. AREA CALCULATOR")
print("=" * 70)


def rectangle(length):

    def area(width):

        return length * width

    return area


calculate = rectangle(10)

print(calculate(5))
print(calculate(8))

# ==========================================================
# EXAMPLE 11
# CLOSURE INSPECTION
# ==========================================================

print("\n" + "=" * 70)
print("11. CLOSURE INFORMATION")
print("=" * 70)

closure = multiplier(5)

print("Function:", closure)

print("Closure:", closure.__closure__)

print("Free Variables:", closure.__code__.co_freevars)

# ==========================================================
# WHY USE CLOSURES?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE CLOSURES?")
print("=" * 70)

advantages = [

    "Remember State",

    "Data Encapsulation",

    "Avoid Global Variables",

    "Reusable Code",

    "Foundation of Decorators",

    "Cleaner Programs"

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

    "Decorators",

    "Caching",

    "Authentication",

    "Logging",

    "Configuration",

    "Callbacks",

    "GUI Programming",

    "API Frameworks",

    "Flask",

    "FastAPI"

]

for item in applications:

    print("✔", item)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting to return the inner function.")
print("❌ Calling inner() instead of returning inner.")
print("❌ Forgetting the nonlocal keyword.")
print("❌ Confusing closures with nested functions.")
print("❌ Modifying outer variables without nonlocal.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use closures to preserve state.")
print("✔ Use nonlocal only when required.")
print("✔ Keep closure logic simple.")
print("✔ Prefer closures over unnecessary global variables.")
print("✔ Use closures as the foundation for decorators.")

# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

questions = [

    "What is a closure?",

    "How is a closure created?",

    "Difference between nested functions and closures?",

    "Why do closures remember variables?",

    "What does nonlocal do?",

    "When should you use closures?",

    "How are closures used in decorators?",

    "Can closures modify outer variables?"

]

for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ A closure is a nested function that remembers")
print("  variables from its enclosing scope.")
print("✔ Closures preserve state between calls.")
print("✔ nonlocal allows modifying outer variables.")
print("✔ Closures avoid unnecessary global variables.")
print("✔ Decorators are built using closures.")

print("=" * 70)
print("End of 03_closures.py")
print("=" * 70)
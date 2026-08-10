# ==========================================================
#       First-Class Functions in Python - Day 19
# ==========================================================

print("=" * 70)
print("         FIRST-CLASS FUNCTIONS IN PYTHON")
print("=" * 70)

"""
A first-class function means that functions are treated
like any other object in Python.

Functions can:
1. Be assigned to variables.
2. Be passed as arguments.
3. Be returned from other functions.
4. Be stored inside data structures.
"""

# ==========================================================
# WHAT ARE FIRST-CLASS FUNCTIONS?
# ==========================================================

print("\nWHAT ARE FIRST-CLASS FUNCTIONS?")
print("-" * 70)

print("Functions in Python are objects.")
print("They can be assigned, passed, returned, and stored.")

# ==========================================================
# SIMPLE FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("1. SIMPLE FUNCTION")
print("=" * 70)


def greet():

    print("Hello, Welcome to Python!")


greet()

# ==========================================================
# FUNCTION ASSIGNED TO A VARIABLE
# ==========================================================

print("\n" + "=" * 70)
print("2. FUNCTION ASSIGNED TO A VARIABLE")
print("=" * 70)


def say_hello():

    print("Hello from say_hello()")


message = say_hello

message()

print("Are both references the same object?")

print(message == say_hello)

# ==========================================================
# FUNCTIONS ARE OBJECTS
# ==========================================================

print("\n" + "=" * 70)
print("3. FUNCTIONS ARE OBJECTS")
print("=" * 70)

print(type(say_hello))

print(id(say_hello))

print(id(message))

# ==========================================================
# PASSING FUNCTION AS ARGUMENT
# ==========================================================

print("\n" + "=" * 70)
print("4. PASS FUNCTION AS ARGUMENT")
print("=" * 70)


def morning():

    print("Good Morning!")


def evening():

    print("Good Evening!")


def greet_user(function):

    print("Calling another function...")

    function()


greet_user(morning)

greet_user(evening)

# ==========================================================
# FUNCTION WITH PARAMETERS
# ==========================================================

print("\n" + "=" * 70)
print("5. PASS FUNCTION WITH PARAMETERS")
print("=" * 70)


def square(number):

    return number ** 2


def cube(number):

    return number ** 3


def calculate(function, value):

    result = function(value)

    print("Result:", result)


calculate(square, 5)

calculate(cube, 5)

# ==========================================================
# RETURNING A FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("6. RETURNING A FUNCTION")
print("=" * 70)


def choose_operation(operation):

    def add(a, b):

        return a + b

    def multiply(a, b):

        return a * b

    if operation == "add":

        return add

    return multiply


operation = choose_operation("add")

print(operation(10, 20))

operation = choose_operation("multiply")

print(operation(10, 20))

# ==========================================================
# STORING FUNCTIONS IN A LIST
# ==========================================================

print("\n" + "=" * 70)
print("7. FUNCTIONS INSIDE A LIST")
print("=" * 70)


def hello():

    print("Hello")


def python():

    print("Python")


def world():

    print("World")


functions = [

    hello,

    python,

    world

]

for function in functions:

    function()

# ==========================================================
# STORING FUNCTIONS IN A DICTIONARY
# ==========================================================

print("\n" + "=" * 70)
print("8. FUNCTIONS INSIDE A DICTIONARY")
print("=" * 70)


def addition(a, b):

    return a + b


def subtraction(a, b):

    return a - b


def multiplication(a, b):

    return a * b


operations = {

    "add": addition,

    "subtract": subtraction,

    "multiply": multiplication

}

print(operations["add"](20, 10))

print(operations["subtract"](20, 10))

print(operations["multiply"](20, 10))

# ==========================================================
# LAMBDA AS FIRST-CLASS FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("9. LAMBDA FUNCTION")
print("=" * 70)

multiply = lambda x, y: x * y

print(multiply(6, 7))

# ==========================================================
# HIGHER-ORDER FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("10. HIGHER-ORDER FUNCTION")
print("=" * 70)

"""
A Higher-Order Function is a function that:

✔ Accepts another function as an argument

OR

✔ Returns another function.
"""


def apply(function, value):

    return function(value)


result = apply(square, 8)

print(result)

# ==========================================================
# FILTER EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("11. FILTER EXAMPLE")
print("=" * 70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_even(number):

    return number % 2 == 0


even_numbers = list(filter(is_even, numbers))

print(even_numbers)

# ==========================================================
# MAP EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("12. MAP EXAMPLE")
print("=" * 70)

numbers = [1, 2, 3, 4, 5]

squares = list(map(square, numbers))

print(squares)

# ==========================================================
# SORTING USING A FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("13. SORTING USING A FUNCTION")
print("=" * 70)

students = [

    ("Rahul", 75),

    ("Ankit", 90),

    ("Priya", 82),

    ("Bhomdev", 95)

]


def marks(student):

    return student[1]


students.sort(key=marks)

print(students)

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Decorators",

    "Callbacks",

    "GUI Programming",

    "Event Handling",

    "API Frameworks",

    "Flask",

    "FastAPI",

    "Django",

    "Sorting",

    "Machine Learning"

]

for item in applications:

    print("✔", item)

# ==========================================================
# ADVANTAGES
# ==========================================================

print("\n" + "=" * 70)
print("ADVANTAGES")
print("=" * 70)

advantages = [

    "Reusable Code",

    "Cleaner Programs",

    "Supports Functional Programming",

    "Flexible Design",

    "Less Code Duplication",

    "Easy to Extend"

]

for item in advantages:

    print("✔", item)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Calling a function instead of passing it.")
print("❌ Writing greet() instead of greet.")
print("❌ Confusing function objects with function calls.")
print("❌ Forgetting functions are objects.")
print("❌ Passing incorrect parameters.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Pass function references, not function calls.")
print("✔ Use higher-order functions when appropriate.")
print("✔ Keep functions small and reusable.")
print("✔ Prefer descriptive function names.")
print("✔ Use lambda only for simple expressions.")

# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

questions = [

    "What are first-class functions?",

    "Are functions objects in Python?",

    "Can functions be assigned to variables?",

    "Can functions be passed as arguments?",

    "Can functions return other functions?",

    "What is a higher-order function?",

    "Difference between passing greet and greet()?",

    "Where are first-class functions used in real projects?"

]

for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Functions are first-class objects.")
print("✔ Functions can be assigned to variables.")
print("✔ Functions can be passed as arguments.")
print("✔ Functions can return other functions.")
print("✔ Functions can be stored in lists and dictionaries.")
print("✔ Higher-order functions accept or return functions.")

print("=" * 70)
print("End of 01_first_class_functions.py")
print("=" * 70)
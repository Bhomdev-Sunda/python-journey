# ==========================================================
#          Nested Functions in Python - Day 19
# ==========================================================

print("=" * 70)
print("           NESTED FUNCTIONS IN PYTHON")
print("=" * 70)

"""
A Nested Function is simply a function defined
inside another function.

Nested functions help us:
✔ Organize code
✔ Hide helper functions
✔ Create closures
✔ Build decorators
"""

# ==========================================================
# WHAT IS A NESTED FUNCTION?
# ==========================================================

print("\nWHAT IS A NESTED FUNCTION?")
print("-" * 70)

print("A nested function is a function")
print("defined inside another function.")

# ==========================================================
# EXAMPLE 1
# SIMPLE NESTED FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("1. SIMPLE NESTED FUNCTION")
print("=" * 70)


def outer():

    print("Outer Function Started")

    def inner():

        print("Inner Function Executed")

    inner()

    print("Outer Function Finished")


outer()

# ==========================================================
# EXAMPLE 2
# ACCESSING OUTER VARIABLE
# ==========================================================

print("\n" + "=" * 70)
print("2. ACCESSING OUTER VARIABLE")
print("=" * 70)


def greeting():

    message = "Welcome to Python"

    def display():

        print(message)

    display()


greeting()

# ==========================================================
# EXAMPLE 3
# LOCAL VARIABLES
# ==========================================================

print("\n" + "=" * 70)
print("3. LOCAL VARIABLES")
print("=" * 70)


def employee():

    company = "OpenAI"

    def details():

        employee_name = "Bhomdev"

        print("Company :", company)

        print("Employee:", employee_name)

    details()


employee()

# ==========================================================
# EXAMPLE 4
# INNER FUNCTION CANNOT BE CALLED DIRECTLY
# ==========================================================

print("\n" + "=" * 70)
print("4. INNER FUNCTION VISIBILITY")
print("=" * 70)


def parent():

    def child():

        print("Child Function")

    child()


parent()

print("Inner functions cannot be accessed")
print("outside the outer function.")

# ==========================================================
# EXAMPLE 5
# RETURNING INNER FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("5. RETURN INNER FUNCTION")
print("=" * 70)


def calculator():

    def add(a, b):

        return a + b

    return add


operation = calculator()

print(operation(20, 30))

# ==========================================================
# EXAMPLE 6
# MULTIPLE INNER FUNCTIONS
# ==========================================================

print("\n" + "=" * 70)
print("6. MULTIPLE INNER FUNCTIONS")
print("=" * 70)


def math_operations():

    def addition(a, b):

        return a + b

    def subtraction(a, b):

        return a - b

    print("Addition:", addition(10, 5))

    print("Subtraction:", subtraction(10, 5))


math_operations()

# ==========================================================
# EXAMPLE 7
# SELECTING AN INNER FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("7. RETURN DIFFERENT INNER FUNCTIONS")
print("=" * 70)


def choose(operation):

    def square(number):

        return number ** 2

    def cube(number):

        return number ** 3

    if operation == "square":

        return square

    return cube


function = choose("square")

print(function(5))

function = choose("cube")

print(function(5))

# ==========================================================
# EXAMPLE 8
# PASSING DATA TO INNER FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("8. PASSING DATA")
print("=" * 70)


def student(name):

    def result(mark):

        print(f"{name} scored {mark} marks.")

    result(92)


student("Rahul")

# ==========================================================
# EXAMPLE 9
# SIMPLE VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("9. INPUT VALIDATION")
print("=" * 70)


def login(username, password):

    def validate():

        return username == "admin" and password == "1234"

    if validate():

        print("Login Successful")

    else:

        print("Invalid Credentials")


login("admin", "1234")

login("guest", "0000")

# ==========================================================
# EXAMPLE 10
# NESTED LOOPS
# ==========================================================

print("\n" + "=" * 70)
print("10. MULTIPLICATION TABLE")
print("=" * 70)


def table(number):

    def generate():

        for i in range(1, 11):

            print(f"{number} x {i} = {number * i}")

    generate()


table(5)

# ==========================================================
# EXAMPLE 11
# SCOPE DEMONSTRATION
# ==========================================================

print("\n" + "=" * 70)
print("11. VARIABLE SCOPE")
print("=" * 70)


def outer_scope():

    x = 100

    def inner_scope():

        print("Value of x:", x)

    inner_scope()


outer_scope()

# ==========================================================
# EXAMPLE 12
# SIMPLE MENU
# ==========================================================

print("\n" + "=" * 70)
print("12. SIMPLE MENU")
print("=" * 70)


def menu():

    def option1():

        print("Dashboard")

    def option2():

        print("Profile")

    def option3():

        print("Logout")

    option1()
    option2()
    option3()


menu()

# ==========================================================
# WHY USE NESTED FUNCTIONS?
# ==========================================================

print("\n" + "=" * 70)
print("WHY USE NESTED FUNCTIONS?")
print("=" * 70)

advantages = [

    "Better Code Organization",

    "Encapsulation",

    "Hide Helper Functions",

    "Improved Readability",

    "Create Closures",

    "Build Decorators"

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

    "Closures",

    "Authentication",

    "Validation",

    "GUI Event Handling",

    "Web Frameworks",

    "Callbacks",

    "Data Processing"

]

for item in applications:

    print("✔", item)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Trying to call an inner function from outside.")
print("❌ Confusing local scope with global scope.")
print("❌ Forgetting to call the inner function.")
print("❌ Returning inner() instead of inner (or vice versa).")
print("❌ Creating unnecessary levels of nesting.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use nested functions only when needed.")
print("✔ Keep helper functions private.")
print("✔ Use meaningful function names.")
print("✔ Avoid excessive nesting.")
print("✔ Use nested functions to prepare for closures and decorators.")

# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

questions = [

    "What is a nested function?",

    "Can an inner function access outer variables?",

    "Can an outer function access inner variables?",

    "Can we return an inner function?",

    "Why do we use nested functions?",

    "How are nested functions related to closures?",

    "Can an inner function be called outside the outer function?",

    "Where are nested functions used in real projects?"

]

for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ A nested function is defined inside another function.")
print("✔ Inner functions can access outer variables.")
print("✔ Outer functions cannot access inner local variables.")
print("✔ Inner functions help organize and hide code.")
print("✔ Nested functions are the foundation of closures.")
print("✔ Decorators are built using nested functions.")

print("=" * 70)
print("End of 02_nested_functions.py")
print("=" * 70)
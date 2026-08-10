# ==========================================================
#              *args + **kwargs Practice
#                         Day 20
# ==========================================================

"""
Day 20 - Practice

Topics Covered:
1. *args
2. **kwargs
3. *args unpacking
4. **kwargs unpacking
5. *args + **kwargs together
6. Argument forwarding
7. Flexible functions
8. Decorator-style wrappers
9. Mini project
10. Interview practice
"""

print("=" * 70)
print("                  DAY 20 PRACTICE")
print("=" * 70)


# ==========================================================
# PRACTICE 1 - SUM USING *args
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 1 - SUM USING *args")
print("=" * 70)


def calculate_sum(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total


result = calculate_sum(10, 20, 30, 40, 50)

print("Numbers:", (10, 20, 30, 40, 50))
print("Total:", result)


# ==========================================================
# PRACTICE 2 - AVERAGE USING *args
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 2 - AVERAGE USING *args")
print("=" * 70)


def calculate_average(*numbers):

    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


result = calculate_average(10, 20, 30, 40, 50)

print("Average:", result)


# ==========================================================
# PRACTICE 3 - FIND MAXIMUM AND MINIMUM
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 3 - MAXIMUM AND MINIMUM")
print("=" * 70)


def find_min_max(*numbers):

    if not numbers:
        return None, None

    return min(numbers), max(numbers)


minimum, maximum = find_min_max(
    45,
    12,
    89,
    23,
    67
)

print("Minimum:", minimum)
print("Maximum:", maximum)


# ==========================================================
# PRACTICE 4 - COUNT EVEN AND ODD NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 4 - EVEN AND ODD")
print("=" * 70)


def count_even_odd(*numbers):

    even_count = 0
    odd_count = 0

    for number in numbers:

        if number % 2 == 0:
            even_count += 1

        else:
            odd_count += 1

    return even_count, odd_count


even, odd = count_even_odd(
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
)

print("Even numbers:", even)
print("Odd numbers:", odd)


# ==========================================================
# PRACTICE 5 - STUDENT PROFILE USING **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 5 - STUDENT PROFILE")
print("=" * 70)


def student_profile(**student):

    print("\n--- STUDENT PROFILE ---")

    for key, value in student.items():

        print(f"{key.title()}: {value}")


student_profile(
    name="Bhomdev",
    age=22,
    course="BCA",
    skill="Python",
    goal="AI Engineer"
)


# ==========================================================
# PRACTICE 6 - USER SETTINGS USING **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 6 - USER SETTINGS")
print("=" * 70)


def user_settings(**settings):

    theme = settings.get("theme", "light")

    language = settings.get("language", "English")

    notifications = settings.get("notifications", True)

    print("Theme:", theme)
    print("Language:", language)
    print("Notifications:", notifications)


user_settings(
    theme="dark",
    notifications=False
)


# ==========================================================
# PRACTICE 7 - DICTIONARY UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 7 - DICTIONARY UNPACKING")
print("=" * 70)


def create_profile(name, age, city, role):

    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Role:", role)


profile_data = {
    "name": "Bhomdev",
    "age": 22,
    "city": "Punjab",
    "role": "Python Developer"
}

create_profile(**profile_data)


# ==========================================================
# PRACTICE 8 - LIST UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 8 - LIST UNPACKING")
print("=" * 70)


def introduce(name, age, city):

    print("Name:", name)
    print("Age:", age)
    print("City:", city)


user_data = [
    "Bhomdev",
    22,
    "Punjab"
]

introduce(*user_data)


# ==========================================================
# PRACTICE 9 - COMBINE *args AND **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 9 - *args + **kwargs")
print("=" * 70)


def show_information(*args, **kwargs):

    print("Positional arguments:")

    for value in args:
        print("-", value)

    print("\nKeyword arguments:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_information(
    10,
    20,
    30,
    name="Bhomdev",
    role="Developer",
    city="Punjab"
)


# ==========================================================
# PRACTICE 10 - FLEXIBLE CALCULATOR
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 10 - FLEXIBLE CALCULATOR")
print("=" * 70)


def calculator(*numbers, **options):

    if not numbers:

        print("No numbers provided.")

        return

    operation = options.get("operation", "add")

    if operation == "add":

        result = sum(numbers)

    elif operation == "subtract":

        result = numbers[0]

        for number in numbers[1:]:

            result -= number

    elif operation == "multiply":

        result = 1

        for number in numbers:

            result *= number

    elif operation == "max":

        result = max(numbers)

    elif operation == "min":

        result = min(numbers)

    else:

        print("Invalid operation.")

        return

    print("Numbers:", numbers)
    print("Operation:", operation)
    print("Result:", result)


calculator(
    10,
    20,
    30,
    operation="add"
)

calculator(
    100,
    20,
    10,
    operation="subtract"
)

calculator(
    2,
    3,
    4,
    operation="multiply"
)

calculator(
    10,
    50,
    30,
    operation="max"
)

calculator(
    10,
    50,
    30,
    operation="min"
)


# ==========================================================
# PRACTICE 11 - SHOPPING CART
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 11 - SHOPPING CART")
print("=" * 70)


def shopping_cart(*prices, **order_details):

    if not prices:

        print("Cart is empty.")

        return

    total = sum(prices)

    print("Items:", len(prices))

    print("Prices:", prices)

    print("Total:", total)

    print("\nOrder Details:")

    for key, value in order_details.items():

        print(f"{key.title()}: {value}")


shopping_cart(
    499,
    799,
    299,
    999,
    customer="Bhomdev",
    payment="UPI",
    city="Punjab"
)


# ==========================================================
# PRACTICE 12 - FUNCTION FORWARDING
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 12 - FUNCTION FORWARDING")
print("=" * 70)


def add_numbers(a, b, c):

    return a + b + c


def execute_function(function, *args, **kwargs):

    return function(*args, **kwargs)


result = execute_function(
    add_numbers,
    10,
    20,
    30
)

print("Result:", result)


# ==========================================================
# PRACTICE 13 - FORWARD KEYWORD ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 13 - FORWARD KEYWORD ARGUMENTS")
print("=" * 70)


def create_account(name, age, city):

    print("Name:", name)
    print("Age:", age)
    print("City:", city)


def forward_account(function, **kwargs):

    function(**kwargs)


account = {
    "name": "Bhomdev",
    "age": 22,
    "city": "Punjab"
}

forward_account(
    create_account,
    **account
)


# ==========================================================
# PRACTICE 14 - COMBINE TWO DICTIONARIES
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 14 - DICTIONARY MERGING")
print("=" * 70)


personal = {
    "name": "Bhomdev",
    "age": 22
}

professional = {
    "role": "Python Developer",
    "skill": "FastAPI"
}

combined = {
    **personal,
    **professional
}

print("Combined dictionary:")

for key, value in combined.items():

    print(f"{key}: {value}")


# ==========================================================
# PRACTICE 15 - OVERRIDE DICTIONARY VALUE
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 15 - OVERRIDE VALUE")
print("=" * 70)


default_config = {
    "theme": "light",
    "language": "English",
    "notifications": True
}

custom_config = {
    "theme": "dark",
    "notifications": False
}

final_config = {
    **default_config,
    **custom_config
}

print("Final configuration:")

for key, value in final_config.items():

    print(f"{key}: {value}")


# ==========================================================
# PRACTICE 16 - DECORATOR WITH *args AND **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 16 - DECORATOR")
print("=" * 70)


def logger(function):

    def wrapper(*args, **kwargs):

        print("\n--- FUNCTION CALL ---")

        print("Function:", function.__name__)

        print("args:", args)

        print("kwargs:", kwargs)

        result = function(*args, **kwargs)

        print("Result:", result)

        return result

    return wrapper


@logger
def multiply(a, b):

    return a * b


multiply(
    10,
    20
)


# ==========================================================
# PRACTICE 17 - DECORATOR WITH MIXED ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 17 - MIXED ARGUMENT DECORATOR")
print("=" * 70)


def monitor(function):

    def wrapper(*args, **kwargs):

        print("\nCalling:", function.__name__)

        result = function(*args, **kwargs)

        print("Execution completed.")

        return result

    return wrapper


@monitor
def introduce_user(name, age, city="Unknown"):

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


introduce_user(
    "Bhomdev",
    22,
    city="Punjab"
)


# ==========================================================
# PRACTICE 18 - API REQUEST SIMULATION
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 18 - API REQUEST")
print("=" * 70)


def api_request(endpoint, *parameters, **options):

    print("\n--- API REQUEST ---")

    print("Endpoint:", endpoint)

    print("Parameters:", parameters)

    print("Options:")

    for key, value in options.items():

        print(f"{key}: {value}")


api_request(
    "/users",
    "page=1",
    "limit=10",
    method="GET",
    timeout=30,
    authentication=True
)


# ==========================================================
# PRACTICE 19 - DATABASE QUERY SIMULATION
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 19 - DATABASE QUERY")
print("=" * 70)


def database_query(query, *values, **options):

    print("\n--- DATABASE QUERY ---")

    print("Query:", query)

    print("Values:", values)

    print("Options:", options)


database_query(
    "SELECT * FROM users WHERE age > ?",
    18,
    database="users_db",
    timeout=10
)


# ==========================================================
# PRACTICE 20 - STARRED ASSIGNMENT
# ==========================================================

print("\n" + "=" * 70)
print("PRACTICE 20 - STARRED ASSIGNMENT")
print("=" * 70)


numbers = [
    10,
    20,
    30,
    40,
    50
]

first, *middle, last = numbers

print("First:", first)

print("Middle:", middle)

print("Last:", last)


# ==========================================================
# MINI PROJECT - FLEXIBLE ORDER SYSTEM
# ==========================================================

print("\n" + "=" * 70)
print("MINI PROJECT - FLEXIBLE ORDER SYSTEM")
print("=" * 70)


def create_order(customer, *items, **details):

    print("\n" + "-" * 50)
    print("                ORDER DETAILS")
    print("-" * 50)

    print("Customer:", customer)

    print("\nItems:")

    if not items:

        print("No items added.")

    else:

        for item in items:

            print("-", item)

    print("\nAdditional Details:")

    if not details:

        print("No additional details.")

    else:

        for key, value in details.items():

            print(f"{key.title()}: {value}")


create_order(
    "Bhomdev",
    "Laptop",
    "Mouse",
    "Keyboard",
    "Headphones",
    payment="UPI",
    city="Punjab",
    delivery="Express"
)


# ==========================================================
# MINI PROJECT - FLEXIBLE STUDENT SYSTEM
# ==========================================================

print("\n" + "=" * 70)
print("MINI PROJECT - STUDENT SYSTEM")
print("=" * 70)


def register_student(name, *subjects, **details):

    print("\n" + "-" * 50)
    print("             STUDENT REGISTRATION")
    print("-" * 50)

    print("Name:", name)

    print("\nSubjects:")

    for subject in subjects:

        print("-", subject)

    print("\nAdditional Details:")

    for key, value in details.items():

        print(f"{key.title()}: {value}")


register_student(
    "Bhomdev",
    "Python",
    "SQL",
    "Machine Learning",
    "Statistics",
    age=22,
    course="BCA",
    goal="AI Engineer"
)


# ==========================================================
# CHALLENGE 1
# ==========================================================

print("\n" + "=" * 70)
print("CHALLENGE 1")
print("=" * 70)

print("""
Create a function called:

calculate_product(*numbers)

Requirements:
1. Accept any number of numbers.
2. Multiply all numbers.
3. Return the result.

Example:

calculate_product(2, 3, 4)

Expected:
24
""")


# ==========================================================
# CHALLENGE 2
# ==========================================================

print("\n" + "=" * 70)
print("CHALLENGE 2")
print("=" * 70)

print("""
Create a function:

show_user(**user)

Requirements:
1. Accept any number of keyword arguments.
2. Print every key and value.

Example:

show_user(
    name="Bhomdev",
    age=22,
    city="Punjab"
)
""")


# ==========================================================
# CHALLENGE 3
# ==========================================================

print("\n" + "=" * 70)
print("CHALLENGE 3")
print("=" * 70)

print("""
Create a function:

process_data(*args, **kwargs)

Requirements:
1. Print all positional arguments.
2. Print all keyword arguments.
3. Display the number of positional arguments.
4. Display the number of keyword arguments.
""")


# ==========================================================
# CHALLENGE 4
# ==========================================================

print("\n" + "=" * 70)
print("CHALLENGE 4")
print("=" * 70)

print("""
Create:

def execute(function, *args, **kwargs):

The function should execute another function
using both positional and keyword arguments.

Example:

execute(
    introduce,
    "Bhomdev",
    age=22,
    city="Punjab"
)
""")


# ==========================================================
# CHALLENGE 5
# ==========================================================

print("\n" + "=" * 70)
print("CHALLENGE 5")
print("=" * 70)

print("""
Create a decorator called:

@logger

The decorator should:

1. Accept any function.
2. Accept any *args.
3. Accept any **kwargs.
4. Print the function name.
5. Print the arguments.
6. Execute the function.
7. Return the result.
""")


# ==========================================================
# DAY 20 KNOWLEDGE CHECK
# ==========================================================

print("\n" + "=" * 70)
print("DAY 20 KNOWLEDGE CHECK")
print("=" * 70)


questions = [
    "What is *args?",
    "What is **kwargs?",
    "What type is args?",
    "What type is kwargs?",
    "What is positional unpacking?",
    "What is dictionary unpacking?",
    "What does *numbers do?",
    "What does **data do?",
    "Can *args and **kwargs be used together?",
    "Why are *args and **kwargs useful in decorators?",
    "How do you forward arguments to another function?",
    "What happens when *args receives no arguments?",
    "What happens when **kwargs receives no arguments?"
]


for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")


# ==========================================================
# FINAL REVISION
# ==========================================================

print("\n" + "=" * 70)
print("FINAL REVISION")
print("=" * 70)

print("""
*args
-----
Collects extra positional arguments.

Type:
tuple


**kwargs
--------
Collects extra keyword arguments.

Type:
dictionary


* unpacking
------------
Unpacks positional values.

Example:

numbers = [10, 20, 30]

function(*numbers)


** unpacking
-------------
Unpacks dictionary values.

Example:

data = {
    "name": "Bhomdev",
    "age": 22
}

function(**data)


Together
--------
A flexible function can use:

def function(*args, **kwargs):
    pass


Forwarding
----------
Arguments can be passed to another function using:

function(*args, **kwargs)


Decorators
----------
This pattern is extremely common:

def wrapper(*args, **kwargs):
    return function(*args, **kwargs)
""")


print("\n" + "=" * 70)
print("          DAY 20 PRACTICE COMPLETED")
print("=" * 70)
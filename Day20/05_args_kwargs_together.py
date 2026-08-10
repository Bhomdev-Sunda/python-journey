# ==========================================================
#           *args + **kwargs Together - Day 20
# ==========================================================

"""
Day 20 - *args and **kwargs Together

Topics Covered:
1. Using *args and **kwargs together
2. Order of parameters
3. How arguments are collected
4. Passing arguments through functions
5. Returning *args and **kwargs
6. Function forwarding
7. Flexible functions
8. Decorator-style wrappers
9. Practical examples
10. Common mistakes
11. Interview questions
"""

print("=" * 70)
print("             *args + **kwargs TOGETHER")
print("=" * 70)


# ==========================================================
# 1. BASIC *args + **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("1. BASIC *args + **kwargs")
print("=" * 70)


def show_data(*args, **kwargs):

    print("Positional arguments:", args)

    print("Keyword arguments:", kwargs)


show_data(
    10,
    20,
    30,
    name="Bhomdev",
    role="Python Developer"
)


# ==========================================================
# 2. UNDERSTANDING THE RESULT
# ==========================================================

print("\n" + "=" * 70)
print("2. UNDERSTANDING THE RESULT")
print("=" * 70)


def demonstrate(*args, **kwargs):

    print("args:", args)

    print("Type of args:", type(args))

    print("kwargs:", kwargs)

    print("Type of kwargs:", type(kwargs))


demonstrate(
    100,
    200,
    300,
    name="Bhomdev",
    age=22
)


# ==========================================================
# 3. EMPTY *args AND **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("3. EMPTY *args AND **kwargs")
print("=" * 70)


def check_arguments(*args, **kwargs):

    print("args:", args)

    print("kwargs:", kwargs)


print("No arguments:")

check_arguments()


print("\nOnly positional arguments:")

check_arguments(10, 20, 30)


print("\nOnly keyword arguments:")

check_arguments(
    name="Bhomdev",
    age=22
)


print("\nBoth:")

check_arguments(
    10,
    20,
    name="Bhomdev",
    age=22
)


# ==========================================================
# 4. NORMAL PARAMETER + *args + **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("4. NORMAL PARAMETER + *args + **kwargs")
print("=" * 70)


def introduce(name, *skills, **details):

    print("Name:", name)

    print("Skills:")

    for skill in skills:

        print("-", skill)

    print("Additional Details:")

    for key, value in details.items():

        print(f"{key}: {value}")


introduce(
    "Bhomdev",
    "Python",
    "SQL",
    "FastAPI",
    "Machine Learning",
    age=22,
    city="Punjab",
    goal="AI Engineer"
)


# ==========================================================
# 5. ARGUMENT COLLECTION
# ==========================================================

print("\n" + "=" * 70)
print("5. ARGUMENT COLLECTION")
print("=" * 70)


def collect_data(*args, **kwargs):

    print("\nCollected positional arguments:")

    for value in args:

        print(value)

    print("\nCollected keyword arguments:")

    for key, value in kwargs.items():

        print(f"{key}: {value}")


collect_data(
    10,
    20,
    30,
    name="Bhomdev",
    age=22,
    skill="Python"
)


# ==========================================================
# 6. PASS *args TO ANOTHER FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("6. PASS *args TO ANOTHER FUNCTION")
print("=" * 70)


def calculate_sum(*numbers):

    return sum(numbers)


def process_numbers(*args):

    result = calculate_sum(*args)

    print("Numbers:", args)

    print("Sum:", result)


process_numbers(10, 20, 30, 40)


# ==========================================================
# 7. PASS **kwargs TO ANOTHER FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("7. PASS **kwargs TO ANOTHER FUNCTION")
print("=" * 70)


def create_profile(name, age, city):

    print("Name:", name)

    print("Age:", age)

    print("City:", city)


def process_profile(**kwargs):

    create_profile(**kwargs)


process_profile(
    name="Bhomdev",
    age=22,
    city="Punjab"
)


# ==========================================================
# 8. PASS *args AND **kwargs TO ANOTHER FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("8. PASS *args AND **kwargs TO ANOTHER FUNCTION")
print("=" * 70)


def target_function(*args, **kwargs):

    print("Target args:", args)

    print("Target kwargs:", kwargs)


def forwarding_function(*args, **kwargs):

    target_function(*args, **kwargs)


forwarding_function(
    10,
    20,
    30,
    name="Bhomdev",
    role="Developer"
)


# ==========================================================
# 9. FUNCTION FORWARDING
# ==========================================================

print("\n" + "=" * 70)
print("9. FUNCTION FORWARDING")
print("=" * 70)


def original_function(*args, **kwargs):

    print("Original function received:")

    print("args:", args)

    print("kwargs:", kwargs)


def wrapper_function(*args, **kwargs):

    print("Wrapper received the arguments.")

    original_function(*args, **kwargs)


wrapper_function(
    100,
    200,
    name="Bhomdev",
    skill="Python"
)


# ==========================================================
# 10. DECORATOR-STYLE WRAPPER
# ==========================================================

print("\n" + "=" * 70)
print("10. DECORATOR-STYLE WRAPPER")
print("=" * 70)


def wrapper(function):

    def inner(*args, **kwargs):

        print("\nBefore function execution")

        result = function(*args, **kwargs)

        print("After function execution")

        return result

    return inner


@wrapper
def greet(name, message):

    print(f"{message}, {name}!")


greet(
    "Bhomdev",
    "Hello"
)


# ==========================================================
# 11. DECORATOR WITH DIFFERENT ARGUMENTS
# ==========================================================

print("\n" + "=" * 70)
print("11. DECORATOR WITH DIFFERENT ARGUMENTS")
print("=" * 70)


def logger(function):

    def inner(*args, **kwargs):

        print("\nFunction:", function.__name__)

        print("Arguments:", args)

        print("Keyword arguments:", kwargs)

        result = function(*args, **kwargs)

        return result

    return inner


@logger
def add(a, b):

    return a + b


result = add(10, 20)

print("Result:", result)


@logger
def introduce_user(name, age, city):

    print(f"User: {name}, {age}, {city}")


introduce_user(
    "Bhomdev",
    22,
    city="Punjab"
)


# ==========================================================
# 12. RETURNING *args
# ==========================================================

print("\n" + "=" * 70)
print("12. RETURNING *args")
print("=" * 70)


def get_numbers(*args):

    return args


numbers = get_numbers(10, 20, 30, 40)

print("Returned:", numbers)

print("Type:", type(numbers))


# ==========================================================
# 13. RETURNING **kwargs
# ==========================================================

print("\n" + "=" * 70)
print("13. RETURNING **kwargs")
print("=" * 70)


def get_details(**kwargs):

    return kwargs


details = get_details(
    name="Bhomdev",
    age=22,
    role="Developer"
)

print("Returned:", details)

print("Type:", type(details))


# ==========================================================
# 14. RETURNING BOTH
# ==========================================================

print("\n" + "=" * 70)
print("14. RETURNING BOTH")
print("=" * 70)


def get_data(*args, **kwargs):

    return args, kwargs


data = get_data(
    10,
    20,
    30,
    name="Bhomdev",
    city="Punjab"
)

print("Returned data:", data)


# ==========================================================
# 15. CALCULATOR USING *args
# ==========================================================

print("\n" + "=" * 70)
print("15. CALCULATOR USING *args")
print("=" * 70)


def calculator(*numbers, **options):

    operation = options.get("operation", "add")

    if not numbers:

        print("No numbers provided.")

        return

    if operation == "add":

        result = sum(numbers)

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
    2,
    3,
    4,
    operation="multiply"
)

calculator(
    10,
    50,
    20,
    operation="max"
)

calculator(
    10,
    50,
    20,
    operation="min"
)


# ==========================================================
# 16. USER PROFILE SYSTEM
# ==========================================================

print("\n" + "=" * 70)
print("16. USER PROFILE SYSTEM")
print("=" * 70)


def create_user(username, *skills, **details):

    print("\n--- USER PROFILE ---")

    print("Username:", username)

    print("Skills:")

    for skill in skills:

        print("-", skill)

    print("Additional Details:")

    for key, value in details.items():

        print(f"{key.title()}: {value}")


create_user(
    "Bhomdev",
    "Python",
    "SQL",
    "FastAPI",
    "Machine Learning",
    age=22,
    city="Punjab",
    experience="Fresher"
)


# ==========================================================
# 17. SHOPPING CART
# ==========================================================

print("\n" + "=" * 70)
print("17. SHOPPING CART")
print("=" * 70)


def shopping_cart(*prices, **details):

    total = sum(prices)

    print("Prices:", prices)

    print("Total:", total)

    print("Order Details:")

    for key, value in details.items():

        print(f"{key}: {value}")


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
# 18. API REQUEST FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("18. API REQUEST FUNCTION")
print("=" * 70)


def api_request(endpoint, *parameters, **options):

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
# 19. DATABASE QUERY FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("19. DATABASE QUERY FUNCTION")
print("=" * 70)


def database_query(query, *values, **options):

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
# 20. FORWARDING FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("20. FORWARDING FUNCTION")
print("=" * 70)


def execute(function, *args, **kwargs):

    print("Executing:", function.__name__)

    return function(*args, **kwargs)


def multiply(a, b, c):

    return a * b * c


result = execute(
    multiply,
    2,
    3,
    4
)

print("Result:", result)


# ==========================================================
# 21. FLEXIBLE PRINT FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("21. FLEXIBLE PRINT FUNCTION")
print("=" * 70)


def flexible_print(*args, **kwargs):

    separator = kwargs.get("sep", " ")

    end = kwargs.get("end", "\n")

    print(*args, sep=separator, end=end)


flexible_print(
    "Python",
    "is",
    "powerful",
    sep=" | "
)


# ==========================================================
# 22. PRACTICAL LOGGING FUNCTION
# ==========================================================

print("\n" + "=" * 70)
print("22. PRACTICAL LOGGING FUNCTION")
print("=" * 70)


def log_message(*messages, **metadata):

    print("\n[LOG]")

    print("Messages:")

    for message in messages:

        print("-", message)

    print("Metadata:")

    for key, value in metadata.items():

        print(f"{key}: {value}")


log_message(
    "User logged in",
    "Dashboard opened",
    user="Bhomdev",
    status="success",
    source="web"
)


# ==========================================================
# 23. ARGUMENT FORWARDING WITH UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("23. ARGUMENT FORWARDING WITH UNPACKING")
print("=" * 70)


def calculate(a, b, c):

    return a + b + c


def forward_calculation(*args, **kwargs):

    return calculate(*args, **kwargs)


numbers = [10, 20, 30]

result = forward_calculation(*numbers)

print("Result:", result)


# ==========================================================
# 24. DICTIONARY FORWARDING
# ==========================================================

print("\n" + "=" * 70)
print("24. DICTIONARY FORWARDING")
print("=" * 70)


def create_account(name, email, city):

    print("Name:", name)

    print("Email:", email)

    print("City:", city)


def forward_account(**kwargs):

    create_account(**kwargs)


account = {
    "name": "Bhomdev",
    "email": "bhomdev@example.com",
    "city": "Punjab"
}

forward_account(**account)


# ==========================================================
# 25. BOTH TYPES OF UNPACKING
# ==========================================================

print("\n" + "=" * 70)
print("25. BOTH TYPES OF UNPACKING")
print("=" * 70)


def display(name, age, *skills, **details):

    print("Name:", name)

    print("Age:", age)

    print("Skills:", skills)

    print("Details:", details)


skills = [
    "Python",
    "SQL",
    "FastAPI"
]

details = {
    "city": "Punjab",
    "goal": "AI Engineer"
}

display(
    "Bhomdev",
    22,
    *skills,
    **details
)


# ==========================================================
# 26. IMPORTANT PARAMETER ORDER
# ==========================================================

print("\n" + "=" * 70)
print("26. IMPORTANT PARAMETER ORDER")
print("=" * 70)

print("""
The general function parameter order is:

1. Positional parameters
2. *args
3. Keyword-only parameters
4. **kwargs

Example:

def function(name, *args, role="Developer", **kwargs):
    pass
""")


# ==========================================================
# 27. ARGUMENT FLOW
# ==========================================================

print("\n" + "=" * 70)
print("27. ARGUMENT FLOW")
print("=" * 70)

print("""
When calling:

function(
    10,
    20,
    30,
    name="Bhomdev",
    age=22
)

The function receives:

args = (10, 20, 30)

kwargs = {
    "name": "Bhomdev",
    "age": 22
}
""")


# ==========================================================
# 28. COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("28. COMMON MISTAKES")
print("=" * 70)

print("❌ Putting **kwargs before *args.")

print("❌ Forgetting to unpack when forwarding arguments.")

print("❌ Using * instead of ** for keyword arguments.")

print("❌ Using ** instead of * for positional arguments.")

print("❌ Passing duplicate keyword arguments.")

print("❌ Assuming args is a list.")

print("❌ Assuming kwargs is a tuple.")

print("❌ Using *args and **kwargs when they are unnecessary.")


# ==========================================================
# 29. BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("29. BEST PRACTICES")
print("=" * 70)

print("✔ Use *args for flexible positional arguments.")

print("✔ Use **kwargs for flexible keyword arguments.")

print("✔ Use *args and **kwargs for argument forwarding.")

print("✔ They are especially useful in decorators.")

print("✔ Use meaningful normal parameters whenever possible.")

print("✔ Don't use them unnecessarily.")

print("✔ Preserve arguments when creating wrappers.")


# ==========================================================
# 30. INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("30. INTERVIEW QUESTIONS")
print("=" * 70)


questions = [

    "What is the difference between *args and **kwargs?",

    "Can *args and **kwargs be used together?",

    "What type is args?",

    "What type is kwargs?",

    "Why are *args and **kwargs commonly used in decorators?",

    "How do you forward *args to another function?",

    "How do you forward **kwargs to another function?",

    "What is argument forwarding?",

    "What is the correct order of function parameters?",

    "What happens when *args receives no arguments?",

    "What happens when **kwargs receives no arguments?",

    "What is the difference between collecting and unpacking?"

]


for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")


# ==========================================================
# 31. FINAL SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("31. FINAL SUMMARY")
print("=" * 70)

print("""
*args
-----
Collects variable positional arguments.

Type:
tuple


**kwargs
--------
Collects variable keyword arguments.

Type:
dictionary


*args + **kwargs
----------------
Allows a function to accept flexible positional
and keyword arguments.


Argument forwarding
-------------------
Use:

function(*args, **kwargs)

to pass collected arguments to another function.


Decorators
----------
Decorators commonly use:

def wrapper(*args, **kwargs):
    return function(*args, **kwargs)

This allows the decorator to work with functions
having different numbers and types of arguments.
""")


print("\n" + "=" * 70)
print("       End of 05_args_kwargs_together.py")
print("=" * 70)
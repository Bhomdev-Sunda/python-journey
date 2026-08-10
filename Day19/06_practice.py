# ==========================================================
#      Day 19 Practice - Functions & Decorators
# ==========================================================

"""
Topics Covered
--------------
1. First-Class Functions
2. Higher-Order Functions
3. Nested Functions
4. Closures
5. nonlocal Keyword
6. Decorators
7. Decorators with Arguments
8. Built-in Decorators
9. @property
10. @staticmethod
11. @classmethod
"""

print("=" * 75)
print("        DAY 19 PRACTICE - FUNCTIONS & DECORATORS")
print("=" * 75)

# ==========================================================
# QUESTION 1
# FIRST-CLASS FUNCTION
# ==========================================================

print("\n1. FIRST-CLASS FUNCTION")
print("-" * 75)


def greet():
    print("Hello Python!")


message = greet

message()

# ==========================================================
# QUESTION 2
# PASS FUNCTION AS ARGUMENT
# ==========================================================

print("\n2. PASS FUNCTION AS ARGUMENT")
print("-" * 75)


def morning():
    print("Good Morning!")


def execute(function):
    function()


execute(morning)

# ==========================================================
# QUESTION 3
# RETURN FUNCTION
# ==========================================================

print("\n3. RETURN FUNCTION")
print("-" * 75)


def calculator():

    def square(number):
        return number ** 2

    return square


operation = calculator()

print(operation(8))

# ==========================================================
# QUESTION 4
# NESTED FUNCTION
# ==========================================================

print("\n4. NESTED FUNCTION")
print("-" * 75)


def outer():

    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()


outer()

# ==========================================================
# QUESTION 5
# CLOSURE
# ==========================================================

print("\n5. CLOSURE")
print("-" * 75)


def multiplier(value):

    def multiply(number):
        return number * value

    return multiply


double = multiplier(2)

print(double(20))

# ==========================================================
# QUESTION 6
# CLOSURE COUNTER
# ==========================================================

print("\n6. CLOSURE COUNTER")
print("-" * 75)


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

# ==========================================================
# QUESTION 7
# BASIC DECORATOR
# ==========================================================

print("\n7. BASIC DECORATOR")
print("-" * 75)


def decorator(function):

    def wrapper():

        print("Before Function")

        function()

        print("After Function")

    return wrapper


@decorator
def hello():
    print("Hello World!")


hello()

# ==========================================================
# QUESTION 8
# DECORATOR WITH PARAMETERS
# ==========================================================

print("\n8. DECORATOR WITH PARAMETERS")
print("-" * 75)


def logger(function):

    def wrapper(*args, **kwargs):

        print(f"Calling {function.__name__}")

        result = function(*args, **kwargs)

        print("Completed")

        return result

    return wrapper


@logger
def add(a, b):
    return a + b


print(add(10, 20))

# ==========================================================
# QUESTION 9
# TIMER DECORATOR
# ==========================================================

print("\n9. TIMER DECORATOR")
print("-" * 75)

import time


def timer(function):

    def wrapper():

        start = time.perf_counter()

        function()

        end = time.perf_counter()

        print(f"Time: {end-start:.6f} sec")

    return wrapper


@timer
def calculate():

    total = 0

    for number in range(500000):

        total += number


calculate()

# ==========================================================
# QUESTION 10
# DECORATOR FACTORY
# ==========================================================

print("\n10. DECORATOR FACTORY")
print("-" * 75)


def repeat(times):

    def decorator(function):

        def wrapper():

            for _ in range(times):
                function()

        return wrapper

    return decorator


@repeat(3)
def welcome():
    print("Welcome!")


welcome()

# ==========================================================
# QUESTION 11
# PROPERTY
# ==========================================================

print("\n11. @property")
print("-" * 75)


class Student:

    def __init__(self, name, marks):

        self.name = name
        self._marks = marks

    @property
    def marks(self):
        return self._marks


student = Student("Bhomdev", 95)

print(student.name)

print(student.marks)

# ==========================================================
# QUESTION 12
# PROPERTY SETTER
# ==========================================================

print("\n12. PROPERTY SETTER")
print("-" * 75)


class Employee:

    def __init__(self, salary):

        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):

        if value >= 0:

            self._salary = value


employee = Employee(40000)

print(employee.salary)

employee.salary = 60000

print(employee.salary)

# ==========================================================
# QUESTION 13
# STATIC METHOD
# ==========================================================

print("\n13. STATIC METHOD")
print("-" * 75)


class Calculator:

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.multiply(8, 9))

# ==========================================================
# QUESTION 14
# CLASS METHOD
# ==========================================================

print("\n14. CLASS METHOD")
print("-" * 75)


class Company:

    company = "OpenAI"

    @classmethod
    def display(cls):

        print(cls.company)


Company.display()

# ==========================================================
# QUESTION 15
# ALTERNATIVE CONSTRUCTOR
# ==========================================================

print("\n15. ALTERNATIVE CONSTRUCTOR")
print("-" * 75)


class User:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):

        name, age = data.split("-")

        return cls(name, int(age))


user = User.from_string("Rahul-22")

print(user.name)

print(user.age)

# ==========================================================
# QUESTION 16
# MAP
# ==========================================================

print("\n16. MAP")
print("-" * 75)

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x ** 2, numbers))

print(result)

# ==========================================================
# QUESTION 17
# FILTER
# ==========================================================

print("\n17. FILTER")
print("-" * 75)

numbers = list(range(1, 21))

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

# ==========================================================
# QUESTION 18
# SORTING
# ==========================================================

print("\n18. SORTING")
print("-" * 75)

students = [

    ("Rahul", 75),

    ("Amit", 92),

    ("Priya", 85)

]

students.sort(key=lambda student: student[1])

print(students)

# ==========================================================
# QUESTION 19
# REAL-LIFE LOGIN DECORATOR
# ==========================================================

print("\n19. LOGIN DECORATOR")
print("-" * 75)

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

    print("Dashboard Loaded")


dashboard()

# ==========================================================
# QUESTION 20
# INTERVIEW REVISION
# ==========================================================

print("\n20. INTERVIEW QUESTIONS")
print("-" * 75)

questions = [

    "What is a first-class function?",

    "What is a higher-order function?",

    "What is a nested function?",

    "What is a closure?",

    "What does nonlocal do?",

    "What is a decorator?",

    "Difference between @property and @staticmethod?",

    "Difference between @staticmethod and @classmethod?",

    "What is a wrapper function?",

    "Give real-life uses of decorators."

]

for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")

# ==========================================================
# KEY TAKEAWAYS
# ==========================================================

print("\n21. KEY TAKEAWAYS")
print("-" * 75)

points = [

    "Functions are first-class objects.",

    "Functions can be passed and returned.",

    "Nested functions improve organization.",

    "Closures preserve state.",

    "nonlocal modifies outer variables.",

    "Decorators extend function behavior.",

    "@property creates computed attributes.",

    "@staticmethod creates utility methods.",

    "@classmethod works with class objects.",

    "Decorators are widely used in FastAPI, Flask and Django."

]

for point in points:
    print("✔", point)

print("\n" + "=" * 75)
print("          DAY 19 PRACTICE COMPLETED SUCCESSFULLY")
print("=" * 75)
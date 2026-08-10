# ==========================================================
#       Built-in Decorators in Python - Day 19
# ==========================================================

print("=" * 70)
print("         BUILT-IN DECORATORS IN PYTHON")
print("=" * 70)

"""
Python provides several built-in decorators.

The most commonly used are:

1. @property
2. @staticmethod
3. @classmethod

These decorators are heavily used in
Object-Oriented Programming (OOP).
"""

# ==========================================================
# WHAT ARE BUILT-IN DECORATORS?
# ==========================================================

print("\nWHAT ARE BUILT-IN DECORATORS?")
print("-" * 70)

print("@property    -> Makes a method behave like an attribute.")
print("@staticmethod -> Utility method (no self or cls).")
print("@classmethod  -> Works with the class (cls).")

# ==========================================================
# 1. @property
# ==========================================================

print("\n" + "=" * 70)
print("1. @property")
print("=" * 70)


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
# PROPERTY WITH SETTER
# ==========================================================

print("\n" + "=" * 70)
print("2. PROPERTY SETTER")
print("=" * 70)


class Employee:

    def __init__(self, salary):

        self._salary = salary

    @property
    def salary(self):

        return self._salary

    @salary.setter
    def salary(self, value):

        if value < 0:

            print("Salary cannot be negative.")

        else:

            self._salary = value


employee = Employee(50000)

print(employee.salary)

employee.salary = 65000

print(employee.salary)

employee.salary = -100

# ==========================================================
# PROPERTY DELETER
# ==========================================================

print("\n" + "=" * 70)
print("3. PROPERTY DELETER")
print("=" * 70)


class User:

    def __init__(self, username):

        self._username = username

    @property
    def username(self):

        return self._username

    @username.deleter
    def username(self):

        print("Username Deleted")

        del self._username


user = User("python_dev")

print(user.username)

del user.username

# ==========================================================
# READ-ONLY PROPERTY
# ==========================================================

print("\n" + "=" * 70)
print("4. READ-ONLY PROPERTY")
print("=" * 70)


class Circle:

    def __init__(self, radius):

        self.radius = radius

    @property
    def area(self):

        return 3.14159 * self.radius ** 2


circle = Circle(5)

print(circle.area)

# ==========================================================
# 2. @staticmethod
# ==========================================================

print("\n" + "=" * 70)
print("5. @staticmethod")
print("=" * 70)


class Calculator:

    @staticmethod
    def add(a, b):

        return a + b

    @staticmethod
    def multiply(a, b):

        return a * b


print(Calculator.add(10, 20))
print(Calculator.multiply(5, 8))

# ==========================================================
# STATIC METHOD EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("6. STATIC METHOD EXAMPLE")
print("=" * 70)


class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):

        return (celsius * 9 / 5) + 32


print(Temperature.celsius_to_fahrenheit(30))

# ==========================================================
# 3. @classmethod
# ==========================================================

print("\n" + "=" * 70)
print("7. @classmethod")
print("=" * 70)


class Company:

    company_name = "OpenAI"

    @classmethod
    def display_company(cls):

        print("Company:", cls.company_name)


Company.display_company()

# ==========================================================
# MODIFY CLASS VARIABLE
# ==========================================================

print("\n" + "=" * 70)
print("8. MODIFY CLASS VARIABLE")
print("=" * 70)


class School:

    school_name = "ABC Public School"

    @classmethod
    def change_school(cls, new_name):

        cls.school_name = new_name


print(School.school_name)

School.change_school("XYZ International School")

print(School.school_name)

# ==========================================================
# ALTERNATIVE CONSTRUCTOR
# ==========================================================

print("\n" + "=" * 70)
print("9. ALTERNATIVE CONSTRUCTOR")
print("=" * 70)


class StudentInfo:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):

        name, age = data.split("-")

        return cls(name, int(age))


student = StudentInfo.from_string("Rahul-21")

print(student.name)
print(student.age)

# ==========================================================
# DIFFERENCE DEMO
# ==========================================================

print("\n" + "=" * 70)
print("10. DIFFERENCE BETWEEN METHODS")
print("=" * 70)


class Demo:

    class_variable = "Python"

    def instance_method(self):

        print("Instance Method")
        print("Uses self")

    @classmethod
    def class_method(cls):

        print("Class Method")
        print("Uses cls")

    @staticmethod
    def static_method():

        print("Static Method")
        print("Uses neither self nor cls")


demo = Demo()

demo.instance_method()

Demo.class_method()

Demo.static_method()

# ==========================================================
# WHEN TO USE WHICH?
# ==========================================================

print("\n" + "=" * 70)
print("WHEN TO USE WHICH?")
print("=" * 70)

print("@property")
print("✔ Getter methods")
print("✔ Read-only attributes")
print("✔ Validation")

print("\n@staticmethod")
print("✔ Utility functions")
print("✔ Calculations")
print("✔ Helper methods")

print("\n@classmethod")
print("✔ Class variables")
print("✔ Alternative constructors")
print("✔ Factory methods")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "@property → Encapsulation",

    "@property → Validation",

    "@staticmethod → Utility Functions",

    "@staticmethod → Calculators",

    "@classmethod → Factory Methods",

    "@classmethod → Configuration",

    "Django Models",

    "Flask",

    "FastAPI",

    "Data Classes"

]

for item in applications:

    print("✔", item)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Using self inside @staticmethod.")
print("❌ Using cls inside instance methods unnecessarily.")
print("❌ Forgetting @property for getters.")
print("❌ Accessing instance variables from static methods.")
print("❌ Confusing @classmethod with @staticmethod.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use @property for computed/read-only attributes.")
print("✔ Use @staticmethod for helper methods.")
print("✔ Use @classmethod for class-level operations.")
print("✔ Keep methods focused on one responsibility.")
print("✔ Choose the simplest decorator that fits the task.")

# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

print("\n" + "=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

questions = [

    "What is @property?",

    "Why use @property instead of getter methods?",

    "What is @staticmethod?",

    "What is @classmethod?",

    "Difference between @staticmethod and @classmethod?",

    "Difference between instance, class, and static methods?",

    "What is an alternative constructor?",

    "When should each decorator be used?"

]

for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ @property creates attribute-like methods.")
print("✔ @staticmethod does not use self or cls.")
print("✔ @classmethod works with the class using cls.")
print("✔ @classmethod can create alternative constructors.")
print("✔ These decorators improve readability and OOP design.")

print("=" * 70)
print("End of 05_built_in_decorators.py")
print("=" * 70)
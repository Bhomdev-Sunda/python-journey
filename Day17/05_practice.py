# ==========================================================
#      Day 17 Practice - Iterables & Iterators in Python
# ==========================================================

"""
Topics Covered
--------------
1. Iterable
2. Iterator
3. iter()
4. next()
5. StopIteration
6. Manual Iteration
7. Custom Iterator
8. Iterator Protocol
9. Real-life Examples
"""

print("=" * 75)
print("      DAY 17 PRACTICE - ITERABLES & ITERATORS")
print("=" * 75)


# ==========================================================
# QUESTION 1
# CHECK WHETHER AN OBJECT IS ITERABLE
# ==========================================================

print("\n1. CHECK ITERABLE")
print("-" * 75)

objects = [
    [1, 2, 3],
    (10, 20),
    {"A": 1},
    {1, 2, 3},
    "Python",
    100,
    5.5,
    True
]

for obj in objects:

    try:

        iter(obj)

        print(f"{obj}  --> Iterable")

    except TypeError:

        print(f"{obj}  --> Not Iterable")


# ==========================================================
# QUESTION 2
# CREATE ITERATOR FROM LIST
# ==========================================================

print("\n2. ITERATOR FROM LIST")
print("-" * 75)

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# ==========================================================
# QUESTION 3
# HANDLE StopIteration
# ==========================================================

print("\n3. HANDLE StopIteration")
print("-" * 75)

numbers = [1, 2]

iterator = iter(numbers)

while True:

    try:

        print(next(iterator))

    except StopIteration:

        print("Iteration Finished")

        break


# ==========================================================
# QUESTION 4
# ITERATE THROUGH STRING
# ==========================================================

print("\n4. STRING ITERATOR")
print("-" * 75)

language = "PYTHON"

iterator = iter(language)

for letter in iterator:

    print(letter)


# ==========================================================
# QUESTION 5
# ITERATE THROUGH DICTIONARY
# ==========================================================

print("\n5. DICTIONARY ITERATION")
print("-" * 75)

student = {

    "Name": "Bhomdev",

    "Age": 22,

    "Course": "Python"

}

iterator = iter(student)

while True:

    try:

        key = next(iterator)

        print(key, ":", student[key])

    except StopIteration:

        break


# ==========================================================
# QUESTION 6
# CUSTOM COUNTER
# ==========================================================

print("\n6. CUSTOM COUNTER")
print("-" * 75)


class Counter:

    def __init__(self, limit):

        self.number = 1

        self.limit = limit

    def __iter__(self):

        return self

    def __next__(self):

        if self.number <= self.limit:

            value = self.number

            self.number += 1

            return value

        raise StopIteration


counter = Counter(5)

for value in counter:

    print(value)


# ==========================================================
# QUESTION 7
# EVEN NUMBER ITERATOR
# ==========================================================

print("\n7. EVEN NUMBERS")
print("-" * 75)


class EvenNumbers:

    def __init__(self, limit):

        self.current = 2

        self.limit = limit

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= self.limit:

            number = self.current

            self.current += 2

            return number

        raise StopIteration


evens = EvenNumbers(20)

for number in evens:

    print(number)


# ==========================================================
# QUESTION 8
# FIBONACCI ITERATOR
# ==========================================================

print("\n8. FIBONACCI")
print("-" * 75)


class Fibonacci:

    def __init__(self, terms):

        self.terms = terms

        self.count = 0

        self.a = 0

        self.b = 1

    def __iter__(self):

        return self

    def __next__(self):

        if self.count >= self.terms:

            raise StopIteration

        value = self.a

        self.a, self.b = self.b, self.a + self.b

        self.count += 1

        return value


fib = Fibonacci(10)

for number in fib:

    print(number)


# ==========================================================
# QUESTION 9
# SQUARE NUMBER ITERATOR
# ==========================================================

print("\n9. SQUARE NUMBERS")
print("-" * 75)


class Squares:

    def __init__(self, limit):

        self.current = 1

        self.limit = limit

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= self.limit:

            square = self.current ** 2

            self.current += 1

            return square

        raise StopIteration


square_iterator = Squares(10)

for square in square_iterator:

    print(square)


# ==========================================================
# QUESTION 10
# ALPHABET ITERATOR
# ==========================================================

print("\n10. ALPHABETS")
print("-" * 75)


class Alphabet:

    def __init__(self):

        self.current = ord("A")

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= ord("Z"):

            letter = chr(self.current)

            self.current += 1

            return letter

        raise StopIteration


letters = Alphabet()

for letter in letters:

    print(letter, end=" ")

print()


# ==========================================================
# QUESTION 11
# next(iterator, default)
# ==========================================================

print("\n11. next(iterator, default)")
print("-" * 75)

numbers = [100, 200]

iterator = iter(numbers)

print(next(iterator, "Finished"))
print(next(iterator, "Finished"))
print(next(iterator, "Finished"))
print(next(iterator, "Finished"))


# ==========================================================
# QUESTION 12
# FOR LOOP INTERNALLY
# ==========================================================

print("\n12. HOW FOR LOOP WORKS")
print("-" * 75)

numbers = [5, 10, 15]

iterator = iter(numbers)

while True:

    try:

        value = next(iterator)

        print(value)

    except StopIteration:

        break


# ==========================================================
# MINI PROJECT
# EMPLOYEE ITERATOR
# ==========================================================

print("\n13. MINI PROJECT - EMPLOYEE ITERATOR")
print("-" * 75)


class EmployeeIterator:

    def __init__(self, employees):

        self.employees = employees

        self.index = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.index < len(self.employees):

            employee = self.employees[self.index]

            self.index += 1

            return employee

        raise StopIteration


employee_list = [

    "Rahul",

    "Priya",

    "Bhomdev",

    "Ankit",

    "Neha"

]

iterator = EmployeeIterator(employee_list)

for employee in iterator:

    print(employee)


# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

print("\n14. QUICK INTERVIEW REVISION")
print("-" * 75)

questions = [

    "What is an iterable?",

    "What is an iterator?",

    "Difference between iterable and iterator?",

    "What does iter() do?",

    "What does next() do?",

    "What is StopIteration?",

    "Why are iterators memory efficient?",

    "What methods are required for a custom iterator?",

    "Difference between __iter__() and __next__()?",

    "Give one real-life use of iterators."

]

for index, question in enumerate(questions, start=1):

    print(f"{index}. {question}")


# ==========================================================
# KEY TAKEAWAYS
# ==========================================================

print("\n15. KEY TAKEAWAYS")
print("-" * 75)

points = [

    "Iterable objects can be looped over.",

    "Iterator objects produce one item at a time.",

    "iter() converts an iterable into an iterator.",

    "next() returns the next element.",

    "StopIteration indicates no more values.",

    "Custom iterators implement __iter__() and __next__().",

    "Iterators use lazy evaluation.",

    "They are memory efficient.",

    "Python for-loops use iterators internally.",

    "Iterators are useful for processing huge datasets."

]

for point in points:

    print("✔", point)

print("\n" + "=" * 75)
print("        DAY 17 PRACTICE COMPLETED SUCCESSFULLY")
print("=" * 75)
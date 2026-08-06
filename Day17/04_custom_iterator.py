# ==========================================================
#          Custom Iterators in Python - Day 17
# ==========================================================

print("=" * 70)
print("             CUSTOM ITERATORS IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS A CUSTOM ITERATOR?
# ==========================================================

"""
A custom iterator is a user-defined class that follows
Python's Iterator Protocol.

To create a custom iterator, we implement:

1. __iter__()
2. __next__()

__iter__() -> Returns the iterator object.
__next__() -> Returns the next value.

When no values remain,
__next__() must raise StopIteration.
"""

print("\nWHAT IS A CUSTOM ITERATOR?")
print("-" * 70)

print("A custom iterator lets us define")
print("our own iteration logic.")

# ==========================================================
# EXAMPLE 1
# COUNTING FROM 1 TO 5
# ==========================================================

print("\n" + "=" * 70)
print("1. SIMPLE COUNTER")
print("=" * 70)


class Counter:

    def __init__(self):

        self.number = 1

    def __iter__(self):

        return self

    def __next__(self):

        if self.number <= 5:

            value = self.number

            self.number += 1

            return value

        raise StopIteration


counter = Counter()

for value in counter:

    print(value)

# ==========================================================
# EXAMPLE 2
# CUSTOM RANGE
# ==========================================================

print("\n" + "=" * 70)
print("2. CUSTOM RANGE")
print("=" * 70)


class MyRange:

    def __init__(self, start, end):

        self.current = start

        self.end = end

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= self.end:

            number = self.current

            self.current += 1

            return number

        raise StopIteration


numbers = MyRange(5, 10)

for num in numbers:

    print(num)

# ==========================================================
# EXAMPLE 3
# EVEN NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("3. EVEN NUMBER ITERATOR")
print("=" * 70)


class EvenNumbers:

    def __init__(self, limit):

        self.current = 2

        self.limit = limit

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= self.limit:

            value = self.current

            self.current += 2

            return value

        raise StopIteration


evens = EvenNumbers(20)

for number in evens:

    print(number)

# ==========================================================
# EXAMPLE 4
# ODD NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("4. ODD NUMBER ITERATOR")
print("=" * 70)


class OddNumbers:

    def __init__(self, limit):

        self.current = 1

        self.limit = limit

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= self.limit:

            value = self.current

            self.current += 2

            return value

        raise StopIteration


odds = OddNumbers(15)

for number in odds:

    print(number)

# ==========================================================
# EXAMPLE 5
# SQUARE NUMBERS
# ==========================================================

print("\n" + "=" * 70)
print("5. SQUARE NUMBER ITERATOR")
print("=" * 70)


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
# EXAMPLE 6
# REVERSE COUNTDOWN
# ==========================================================

print("\n" + "=" * 70)
print("6. COUNTDOWN")
print("=" * 70)


class Countdown:

    def __init__(self, start):

        self.current = start

    def __iter__(self):

        return self

    def __next__(self):

        if self.current >= 1:

            value = self.current

            self.current -= 1

            return value

        raise StopIteration


countdown = Countdown(5)

for value in countdown:

    print(value)

# ==========================================================
# EXAMPLE 7
# MANUAL next()
# ==========================================================

print("\n" + "=" * 70)
print("7. MANUAL next()")
print("=" * 70)

counter = Counter()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

try:

    print(next(counter))

except StopIteration:

    print("Counter Finished.")

# ==========================================================
# EXAMPLE 8
# FIBONACCI ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("8. FIBONACCI ITERATOR")
print("=" * 70)


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
# EXAMPLE 9
# ALPHABET ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("9. ALPHABET ITERATOR")
print("=" * 70)


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
# ITERATOR PROTOCOL
# ==========================================================

print("\n" + "=" * 70)
print("ITERATOR PROTOCOL")
print("=" * 70)

print("✔ __iter__() returns the iterator object.")
print("✔ __next__() returns one item.")
print("✔ Raise StopIteration when finished.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Large File Reading",

    "Streaming Data",

    "API Pagination",

    "Database Records",

    "Machine Learning",

    "Game Loops",

    "Log Processing",

    "Infinite Data Streams"

]

for app in applications:

    print("✔", app)

# ==========================================================
# ADVANTAGES
# ==========================================================

print("\n" + "=" * 70)
print("ADVANTAGES")
print("=" * 70)

advantages = [

    "Memory Efficient",

    "Lazy Evaluation",

    "Reusable Logic",

    "Professional Code",

    "Handles Huge Data",

    "Custom Traversal"

]

for item in advantages:

    print("✔", item)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Forgetting __iter__()")
print("❌ Forgetting StopIteration")
print("❌ Infinite loops accidentally")
print("❌ Returning wrong values")
print("❌ Confusing iterables with iterators")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Always implement both __iter__() and __next__().")
print("✔ Raise StopIteration correctly.")
print("✔ Keep iterator logic simple.")
print("✔ Use descriptive variable names.")
print("✔ Test edge cases.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Custom iterators follow the iterator protocol.")
print("✔ __iter__() returns the iterator object.")
print("✔ __next__() returns one value at a time.")
print("✔ StopIteration signals completion.")
print("✔ Custom iterators enable lazy, memory-efficient iteration.")
print("✔ They are useful for large datasets and custom traversal logic.")

print("=" * 70)
print("End of 04_custom_iterator.py")
print("=" * 70)
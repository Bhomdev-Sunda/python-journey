# ==========================================================
#         Understanding Iterators in Python - Day 17
# ==========================================================

print("=" * 70)
print("           UNDERSTANDING ITERATORS IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS AN ITERATOR?
# ==========================================================

# Iterator:
# An iterator is an object that returns one element
# at a time from an iterable.
#
# It remembers its current position.

print("\nWHAT IS AN ITERATOR?")
print("-" * 70)

print("An iterator is an object that")
print("returns one value at a time.")
print("It keeps track of its current position.")

# ==========================================================
# WHY DO WE USE ITERATORS?
# ==========================================================

print("\n" + "=" * 70)
print("WHY DO WE USE ITERATORS?")
print("=" * 70)

print("1. Memory Efficient")
print("2. Process Large Data")
print("3. Lazy Evaluation")
print("4. One Item at a Time")
print("5. Used Internally by for-loops")

# ==========================================================
# ITERABLE vs ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("ITERABLE vs ITERATOR")
print("=" * 70)

print("Iterable")
print("--------")
print("✔ Can be converted into an iterator.")
print("✔ Examples: list, tuple, string.")

print()

print("Iterator")
print("--------")
print("✔ Produces one value at a time.")
print("✔ Created using iter().")
print("✔ Uses next().")

# ==========================================================
# CREATING AN ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("1. CREATING AN ITERATOR")
print("=" * 70)

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print("Iterable :", numbers)
print("Iterator :", iterator)

# ==========================================================
# TYPE OF ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("2. TYPE OF ITERATOR")
print("=" * 70)

print(type(iterator))

# ==========================================================
# USING next()
# ==========================================================

print("\n" + "=" * 70)
print("3. USING next()")
print("=" * 70)

numbers = [100, 200, 300]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# ==========================================================
# StopIteration EXCEPTION
# ==========================================================

print("\n" + "=" * 70)
print("4. StopIteration")
print("=" * 70)

numbers = [1, 2]

iterator = iter(numbers)

try:

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

except StopIteration:

    print("No more elements left.")

# ==========================================================
# ITERATING MANUALLY
# ==========================================================

print("\n" + "=" * 70)
print("5. MANUAL ITERATION")
print("=" * 70)

names = ["Amit", "Rahul", "Bhomdev"]

iterator = iter(names)

while True:

    try:

        value = next(iterator)

        print(value)

    except StopIteration:

        print("Iteration Finished.")

        break

# ==========================================================
# STRING ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("6. STRING ITERATOR")
print("=" * 70)

language = "Python"

iterator = iter(language)

for character in iterator:

    print(character)

# ==========================================================
# TUPLE ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("7. TUPLE ITERATOR")
print("=" * 70)

fruits = ("Apple", "Banana", "Mango")

iterator = iter(fruits)

for fruit in iterator:

    print(fruit)

# ==========================================================
# DICTIONARY ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("8. DICTIONARY ITERATOR")
print("=" * 70)

student = {

    "Name": "Bhomdev",

    "Age": 22,

    "Course": "Python"

}

iterator = iter(student)

for key in iterator:

    print(key)

# ==========================================================
# SET ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("9. SET ITERATOR")
print("=" * 70)

colors = {

    "Red",

    "Blue",

    "Green"

}

iterator = iter(colors)

for color in iterator:

    print(color)

# ==========================================================
# RANGE ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("10. RANGE ITERATOR")
print("=" * 70)

numbers = range(1, 6)

iterator = iter(numbers)

for number in iterator:

    print(number)

# ==========================================================
# CHECKING __iter__()
# ==========================================================

print("\n" + "=" * 70)
print("11. __iter__()")
print("=" * 70)

numbers = [10, 20, 30]

iterator = numbers.__iter__()

print(iterator)

# ==========================================================
# CHECKING __next__()
# ==========================================================

print("\n" + "=" * 70)
print("12. __next__()")
print("=" * 70)

numbers = [5, 10, 15]

iterator = iter(numbers)

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

# ==========================================================
# MEMORY EFFICIENCY
# ==========================================================

print("\n" + "=" * 70)
print("13. MEMORY EFFICIENCY")
print("=" * 70)

large_range = range(1, 1_000_001)

iterator = iter(large_range)

print("First :", next(iterator))
print("Second:", next(iterator))
print("Third :", next(iterator))

print("Only one element is produced at a time.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Reading Huge Files",

    "Database Records",

    "API Responses",

    "CSV Processing",

    "Log File Analysis",

    "Streaming Data",

    "Machine Learning Pipelines",

    "Web Scraping"

]

for app in applications:

    print("✔", app)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Calling next() on a list directly.")
print("❌ Forgetting iter() before next().")
print("❌ Ignoring StopIteration.")
print("❌ Confusing iterable with iterator.")
print("❌ Reusing an exhausted iterator.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use for-loops whenever possible.")
print("✔ Use next() only for manual iteration.")
print("✔ Handle StopIteration.")
print("✔ Prefer iterators for large datasets.")
print("✔ Understand the iterator protocol.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Every iterator is an iterable.")
print("✔ Not every iterable is an iterator.")
print("✔ iter() creates an iterator.")
print("✔ next() retrieves one item at a time.")
print("✔ StopIteration indicates the iterator is exhausted.")
print("✔ Python for-loops automatically use iterators.")

print("=" * 70)
print("End of 02_iterators.py")
print("=" * 70)
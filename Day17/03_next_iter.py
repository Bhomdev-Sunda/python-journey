# ==========================================================
#          iter() and next() Functions in Python
# ==========================================================
print("=" * 70)
print("           iter() AND next() IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS iter()?
# ==========================================================

# iter() converts an iterable into an iterator.

print("\nWHAT IS iter()?")

print("-" * 70)

print("iter() converts an iterable object into an iterator.")
print("After creating an iterator, we can retrieve")
print("elements one at a time using next().")

# ==========================================================
# WHAT IS next()?
# ==========================================================

print("\nWHAT IS next()?")

print("-" * 70)

print("next() returns the next value from an iterator.")
print("When no values remain, it raises StopIteration.")

# ==========================================================
# LIST EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("1. LIST EXAMPLE")
print("=" * 70)

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print("Iterator Created Successfully")

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# ==========================================================
# STRING EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("2. STRING EXAMPLE")
print("=" * 70)

language = "Python"

iterator = iter(language)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# ==========================================================
# TUPLE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("3. TUPLE EXAMPLE")
print("=" * 70)

fruits = ("Apple", "Banana", "Mango")

iterator = iter(fruits)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# ==========================================================
# SET EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("4. SET EXAMPLE")
print("=" * 70)

colors = {"Red", "Green", "Blue"}

iterator = iter(colors)

for color in iterator:

    print(color)

# ==========================================================
# DICTIONARY EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("5. DICTIONARY EXAMPLE")
print("=" * 70)

student = {

    "Name": "Bhomdev",

    "Age": 22,

    "Course": "Python"

}

iterator = iter(student)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# ==========================================================
# RANGE EXAMPLE
# ==========================================================

print("\n" + "=" * 70)
print("6. RANGE EXAMPLE")
print("=" * 70)

numbers = range(1, 6)

iterator = iter(numbers)

for number in iterator:

    print(number)

# ==========================================================
# STOP ITERATION
# ==========================================================

print("\n" + "=" * 70)
print("7. StopIteration EXAMPLE")
print("=" * 70)

numbers = [1, 2]

iterator = iter(numbers)

try:

    while True:

        print(next(iterator))

except StopIteration:

    print("No More Elements.")

# ==========================================================
# next(iterator, default)
# ==========================================================

print("\n" + "=" * 70)
print("8. next(iterator, default)")
print("=" * 70)

numbers = [100, 200]

iterator = iter(numbers)

print(next(iterator, "Finished"))
print(next(iterator, "Finished"))
print(next(iterator, "Finished"))
print(next(iterator, "Finished"))

# ==========================================================
# USING while LOOP
# ==========================================================

print("\n" + "=" * 70)
print("9. MANUAL ITERATION")
print("=" * 70)

names = ["Amit", "Rahul", "Neha"]

iterator = iter(names)

while True:

    value = next(iterator, None)

    if value is None:

        break

    print(value)

# ==========================================================
# FOR LOOP INTERNALLY
# ==========================================================

print("\n" + "=" * 70)
print("10. HOW for LOOP WORKS")
print("=" * 70)

numbers = [10, 20, 30]

iterator = iter(numbers)

while True:

    try:

        item = next(iterator)

        print(item)

    except StopIteration:

        break

print("\nPython for-loop internally works similarly.")

# ==========================================================
# __iter__()
# ==========================================================

print("\n" + "=" * 70)
print("11. __iter__()")
print("=" * 70)

numbers = [1, 2, 3]

iterator = numbers.__iter__()

print(iterator)

# ==========================================================
# __next__()
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
# ITERATOR EXHAUSTION
# ==========================================================

print("\n" + "=" * 70)
print("13. ITERATOR EXHAUSTION")
print("=" * 70)

numbers = [1, 2]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

try:

    print(next(iterator))

except StopIteration:

    print("Iterator Exhausted.")

# ==========================================================
# LARGE DATA
# ==========================================================

print("\n" + "=" * 70)
print("14. LARGE DATA EXAMPLE")
print("=" * 70)

large_numbers = range(1, 1000001)

iterator = iter(large_numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("Only required values are loaded.")

# ==========================================================
# REAL-LIFE APPLICATIONS
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE APPLICATIONS")
print("=" * 70)

applications = [

    "Reading Large Files",

    "Database Records",

    "API Pagination",

    "CSV Processing",

    "Streaming Services",

    "Machine Learning",

    "Big Data",

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

print("❌ Calling next() on a list.")
print("❌ Forgetting iter().")
print("❌ Ignoring StopIteration.")
print("❌ Reusing exhausted iterators.")
print("❌ Confusing iterable with iterator.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use for-loops whenever possible.")
print("✔ Use next() only for manual control.")
print("✔ Handle StopIteration.")
print("✔ Prefer iterators for large datasets.")
print("✔ Understand iterator protocol.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ iter() creates an iterator.")
print("✔ next() returns the next element.")
print("✔ StopIteration ends iteration.")
print("✔ next(iterator, default) avoids exceptions.")
print("✔ for-loops automatically use iter() and next().")
print("✔ Iterators are memory efficient.")

print("=" * 70)
print("End of 03_next_iter.py")
print("=" * 70)
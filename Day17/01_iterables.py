# ==========================================================
#         Understanding Iterables in Python - Day 17
# ==========================================================

print("=" * 70)
print("           UNDERSTANDING ITERABLES IN PYTHON")
print("=" * 70)

# ==========================================================
# WHAT IS AN ITERABLE?
# ==========================================================

# Iterable:
# An iterable is any Python object that can be
# traversed (iterated) one element at a time.

print("\nWHAT IS AN ITERABLE?")
print("-" * 70)

print("An iterable is an object whose elements")
print("can be accessed one by one.")
print("Examples: list, tuple, string, dictionary, set.")

# ==========================================================
# WHY DO WE USE ITERABLES?
# ==========================================================

print("\n" + "=" * 70)
print("WHY DO WE USE ITERABLES?")
print("=" * 70)

print("1. To loop through data.")
print("2. To process collections.")
print("3. To avoid writing repetitive code.")
print("4. To work efficiently with Python loops.")
print("5. To build iterators and generators.")

# ==========================================================
# LIST IS AN ITERABLE
# ==========================================================

print("\n" + "=" * 70)
print("1. LIST ITERABLE")
print("=" * 70)

numbers = [10, 20, 30, 40, 50]

print("List :", numbers)

for number in numbers:

    print(number)

# ==========================================================
# TUPLE IS AN ITERABLE
# ==========================================================

print("\n" + "=" * 70)
print("2. TUPLE ITERABLE")
print("=" * 70)

fruits = ("Apple", "Banana", "Mango")

print("Tuple :", fruits)

for fruit in fruits:

    print(fruit)

# ==========================================================
# STRING IS AN ITERABLE
# ==========================================================

print("\n" + "=" * 70)
print("3. STRING ITERABLE")
print("=" * 70)

language = "Python"

print("String :", language)

for character in language:

    print(character)

# ==========================================================
# DICTIONARY IS AN ITERABLE
# ==========================================================

print("\n" + "=" * 70)
print("4. DICTIONARY ITERABLE")
print("=" * 70)

student = {

    "Name": "Bhomdev",

    "Age": 22,

    "Course": "Python"

}

print(student)

print("\nLooping through keys:")

for key in student:

    print(key)

print("\nLooping through values:")

for value in student.values():

    print(value)

print("\nLooping through items:")

for key, value in student.items():

    print(key, ":", value)

# ==========================================================
# SET IS AN ITERABLE
# ==========================================================

print("\n" + "=" * 70)
print("5. SET ITERABLE")
print("=" * 70)

colors = {

    "Red",

    "Blue",

    "Green",

    "Yellow"

}

print(colors)

for color in colors:

    print(color)

# ==========================================================
# RANGE IS AN ITERABLE
# ==========================================================

print("\n" + "=" * 70)
print("6. RANGE ITERABLE")
print("=" * 70)

numbers = range(1, 6)

for number in numbers:

    print(number)

# ==========================================================
# CHECKING ITERABLE USING iter()
# ==========================================================

print("\n" + "=" * 70)
print("7. USING iter()")
print("=" * 70)

numbers = [1, 2, 3]

iterator = iter(numbers)

print("Iterator Object :", iterator)

# ==========================================================
# TYPE OF ITERATOR
# ==========================================================

print("\n" + "=" * 70)
print("8. TYPE OF ITERATOR")
print("=" * 70)

print(type(iterator))

# ==========================================================
# CHECK DIFFERENT OBJECTS
# ==========================================================

print("\n" + "=" * 70)
print("9. CONVERTING ITERABLES TO ITERATORS")
print("=" * 70)

print(iter("Python"))

print(iter((10, 20, 30)))

print(iter({1, 2, 3}))

print(iter({"A": 1, "B": 2}))

# ==========================================================
# NON-ITERABLE OBJECT
# ==========================================================

print("\n" + "=" * 70)
print("10. NON-ITERABLE OBJECT")
print("=" * 70)

number = 100

try:

    iter(number)

except TypeError as error:

    print(error)

# ==========================================================
# COMMON ITERABLE OBJECTS
# ==========================================================

print("\n" + "=" * 70)
print("COMMON ITERABLE OBJECTS")
print("=" * 70)

iterables = [

    "List",

    "Tuple",

    "Dictionary",

    "Set",

    "String",

    "Range",

    "File Object",

    "Bytes",

    "Bytearray"

]

for item in iterables:

    print("✔", item)

# ==========================================================
# ITERABLE vs NON-ITERABLE
# ==========================================================

print("\n" + "=" * 70)
print("ITERABLE vs NON-ITERABLE")
print("=" * 70)

print("Iterable Objects")
print("----------------")

print("✔ list")
print("✔ tuple")
print("✔ string")
print("✔ dictionary")
print("✔ set")
print("✔ range")

print()

print("Non-Iterable Objects")
print("--------------------")

print("❌ int")
print("❌ float")
print("❌ bool")
print("❌ complex")

# ==========================================================
# REAL-LIFE EXAMPLES
# ==========================================================

print("\n" + "=" * 70)
print("REAL-LIFE EXAMPLES")
print("=" * 70)

examples = [

    "Student List",

    "Employee Records",

    "Shopping Cart",

    "File Lines",

    "Database Records",

    "Product Catalog",

    "Chat Messages",

    "Orders"

]

for example in examples:

    print("✔", example)

# ==========================================================
# BENEFITS OF ITERABLES
# ==========================================================

print("\n" + "=" * 70)
print("BENEFITS OF ITERABLES")
print("=" * 70)

benefits = [

    "Easy Looping",

    "Cleaner Code",

    "Supports for Loop",

    "Reusable",

    "Memory Efficient (with iterators)",

    "Foundation for Generators"

]

for benefit in benefits:

    print("✔", benefit)

# ==========================================================
# COMMON MISTAKES
# ==========================================================

print("\n" + "=" * 70)
print("COMMON MISTAKES")
print("=" * 70)

print("❌ Assuming every object is iterable.")
print("❌ Forgetting to use iter() before next().")
print("❌ Confusing iterable with iterator.")
print("❌ Modifying collections while iterating.")
print("❌ Expecting sets to preserve insertion order.")

# ==========================================================
# BEST PRACTICES
# ==========================================================

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)

print("✔ Use for-loops for iteration.")
print("✔ Use iter() only when manual iteration is needed.")
print("✔ Prefer descriptive variable names.")
print("✔ Handle TypeError when required.")
print("✔ Learn iterator protocol for advanced Python.")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("✔ Iterable objects can be traversed.")
print("✔ Lists, tuples, sets, strings, dictionaries and ranges are iterable.")
print("✔ iter() converts an iterable into an iterator.")
print("✔ Integers and floats are not iterable.")
print("✔ Iterables are the foundation of loops and iterators.")

print("=" * 70)
print("End of 01_iterables.py")
print("=" * 70)
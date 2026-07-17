#                Python Sets 
print("=" * 60)
print("              PYTHON SET BASICS")
print("=" * 60)

# ==========================================================
# WHAT IS A SET?
# ==========================================================

# A set is an unordered collection of unique elements.
# Sets automatically remove duplicate values.

numbers = {10, 20, 30, 40, 50}

print("\nOriginal Set")
print(numbers)

# ==========================================================
# SET REMOVES DUPLICATES
# ==========================================================

marks = {90, 85, 90, 75, 85, 95, 90}

print("\nDuplicate Values Example")
print(marks)

# ==========================================================
# SET CAN STORE DIFFERENT DATA TYPES
# ==========================================================

mixed_data = {
    101,
    "Python",
    99.5,
    True
}

print("\nMixed Data Types")
print(mixed_data)

# ==========================================================
# EMPTY SET
# ==========================================================

empty_set = set()

print("\nEmpty Set")
print(empty_set)

print("Type :", type(empty_set))

# ==========================================================
# EMPTY DICTIONARY VS EMPTY SET
# ==========================================================

empty_dict = {}

print("\nEmpty Dictionary")
print(empty_dict)

print("Type :", type(empty_dict))

# ==========================================================
# SET CREATED FROM A LIST
# ==========================================================

fruits = ["Apple", "Mango", "Apple", "Banana", "Orange", "Mango"]

fruit_set = set(fruits)

print("\nList Converted to Set")
print(fruit_set)

# ==========================================================
# SET CREATED FROM A STRING
# ==========================================================

text = "PYTHON"

letters = set(text)

print("\nString Converted to Set")
print(letters)

# ==========================================================
# SET CREATED FROM A TUPLE
# ==========================================================

numbers_tuple = (1, 2, 3, 4, 5, 5, 2)

tuple_set = set(numbers_tuple)

print("\nTuple Converted to Set")
print(tuple_set)

# ==========================================================
# LENGTH OF A SET
# ==========================================================

print("\nLength of Set")

print(len(numbers))

# ==========================================================
# MEMBERSHIP OPERATOR
# ==========================================================

print("\nMembership Operator")

print(20 in numbers)

print(100 in numbers)

print(50 not in numbers)

# ==========================================================
# LOOPING THROUGH A SET
# ==========================================================

print("\nLooping Through Set")

for value in numbers:
    print(value)

# ==========================================================
# UNORDERED NATURE OF SET
# ==========================================================

print("\nUnordered Set")

colors = {"Red", "Blue", "Green", "Yellow"}

print(colors)

# ==========================================================
# UNIQUE VALUES EXAMPLE
# ==========================================================

cities = {
    "Delhi",
    "Mumbai",
    "Delhi",
    "Chandigarh",
    "Patiala",
    "Mumbai"
}

print("\nUnique Cities")
print(cities)

# ==========================================================
# REAL-LIFE EXAMPLE
# ==========================================================

print("\nStudent Attendance")

attendance = {
    "Rahul",
    "Aman",
    "Bhomdev",
    "Rahul",
    "Priya",
    "Aman"
}

print(attendance)

print("Total Present Students :", len(attendance))

# ==========================================================
# REMOVE DUPLICATES FROM LIST
# ==========================================================

print("\nRemove Duplicates From List")

data = [10, 20, 20, 30, 40, 30, 50, 10]

unique_data = list(set(data))

print("Original List :", data)
print("Unique List   :", unique_data)

# ==========================================================
# TYPE CHECKING
# ==========================================================

print("\nData Type")

print(type(numbers))

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("✔ Set stores unique values.")
print("✔ Duplicate values are removed automatically.")
print("✔ Sets are unordered.")
print("✔ Sets are mutable.")
print("✔ Sets cannot contain mutable elements like lists.")
print("✔ Empty set is created using set().")
print("✔ Curly braces {} without values create a dictionary.")
print("✔ Sets support membership operators (in, not in).")
print("✔ Sets are commonly used to remove duplicates.")
print("✔ Sets can be created from lists, tuples and strings.")

print("=" * 60)
print("End of sets.py")
print("=" * 60)
#              Python Frozen Set 
print("=" * 65)
print("                PYTHON FROZENSET")
print("=" * 65)

# ==========================================================
# WHAT IS A FROZENSET?
# ==========================================================

# A frozenset is an immutable version of a set.
# Once created, you cannot add, remove or modify elements.

numbers = frozenset({10, 20, 30, 40, 50})

print("\nOriginal Frozen Set")
print(numbers)

# ==========================================================
# TYPE OF FROZENSET
# ==========================================================

print("\nData Type")

print(type(numbers))

# ==========================================================
# LENGTH OF FROZENSET
# ==========================================================

print("\nLength")

print(len(numbers))

# ==========================================================
# MEMBERSHIP OPERATORS
# ==========================================================

print("\nMembership Operators")

print("20 in numbers :", 20 in numbers)

print("100 in numbers :", 100 in numbers)

print("40 not in numbers :", 40 not in numbers)

# ==========================================================
# LOOPING THROUGH FROZENSET
# ==========================================================

print("\nLoop Through Frozen Set")

for value in numbers:
    print(value)

# ==========================================================
# DUPLICATE VALUES
# ==========================================================

print("\nDuplicate Values Example")

duplicate = frozenset([1, 2, 2, 3, 4, 4, 5])

print(duplicate)

# ==========================================================
# CREATE FROZENSET FROM LIST
# ==========================================================

print("\nCreate From List")

fruits = ["Apple", "Banana", "Apple", "Orange"]

fruit_set = frozenset(fruits)

print(fruit_set)

# ==========================================================
# CREATE FROZENSET FROM TUPLE
# ==========================================================

print("\nCreate From Tuple")

colors = ("Red", "Blue", "Green", "Blue")

color_set = frozenset(colors)

print(color_set)

# ==========================================================
# CREATE FROZENSET FROM STRING
# ==========================================================

print("\nCreate From String")

text = "PYTHON"

letters = frozenset(text)

print(letters)

# ==========================================================
# SET OPERATIONS
# ==========================================================

print("\n" + "=" * 65)
print("SET OPERATIONS")
print("=" * 65)

A = frozenset({1, 2, 3, 4})

B = frozenset({3, 4, 5, 6})

print("A :", A)
print("B :", B)

# ----------------------------------------------------------
# union()
# ----------------------------------------------------------

print("\nUnion")

print(A.union(B))

# ----------------------------------------------------------
# intersection()
# ----------------------------------------------------------

print("\nIntersection")

print(A.intersection(B))

# ----------------------------------------------------------
# difference()
# ----------------------------------------------------------

print("\nDifference (A - B)")

print(A.difference(B))

# ----------------------------------------------------------
# symmetric_difference()
# ----------------------------------------------------------

print("\nSymmetric Difference")

print(A.symmetric_difference(B))

# ----------------------------------------------------------
# issubset()
# ----------------------------------------------------------

print("\nSubset")

small = frozenset({1, 2})

print(small.issubset(A))

# ----------------------------------------------------------
# issuperset()
# ----------------------------------------------------------

print("\nSuperset")

print(A.issuperset(small))

# ----------------------------------------------------------
# isdisjoint()
# ----------------------------------------------------------

print("\nDisjoint")

X = frozenset({10, 20})

Y = frozenset({30, 40})

print(X.isdisjoint(Y))

# ==========================================================
# IMMUTABLE NATURE
# ==========================================================

print("\n" + "=" * 65)
print("IMMUTABLE NATURE")
print("=" * 65)

print("A frozenset cannot be modified after creation.")

print("\nThe following methods are NOT available:")
print("❌ add()")
print("❌ update()")
print("❌ remove()")
print("❌ discard()")
print("❌ pop()")
print("❌ clear()")

# Uncomment these lines one by one to see the errors.

# numbers.add(60)
# numbers.remove(20)
# numbers.pop()
# numbers.clear()

# ==========================================================
# USING FROZENSET AS A DICTIONARY KEY
# ==========================================================

print("\n" + "=" * 65)
print("FROZENSET AS DICTIONARY KEY")
print("=" * 65)

student_marks = {

    frozenset({"Python", "SQL"}): 95,

    frozenset({"Java", "C++"}): 88

}

for subjects, marks in student_marks.items():

    print(subjects, ":", marks)

# ==========================================================
# REAL-LIFE EXAMPLE
# ==========================================================

print("\n" + "=" * 65)
print("REAL-LIFE EXAMPLE")
print("=" * 65)

permissions = frozenset({

    "Read",

    "Write",

    "Execute"

})

print("Default Permissions")

for permission in permissions:
    print(permission)

print("\nPermissions remain unchanged throughout the program.")

# ==========================================================
# DIFFERENCE BETWEEN SET AND FROZENSET
# ==========================================================

print("\n" + "=" * 65)
print("SET VS FROZENSET")
print("=" * 65)

print("Set")
print("✔ Mutable")
print("✔ Can add elements")
print("✔ Can remove elements")
print("✔ Can update elements")

print("\nFrozen Set")
print("✔ Immutable")
print("✔ Cannot add elements")
print("✔ Cannot remove elements")
print("✔ Cannot update elements")

# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 65)
print("SUMMARY")
print("=" * 65)

print("✔ frozenset is an immutable version of set.")
print("✔ Duplicate values are removed automatically.")
print("✔ Supports union(), intersection(), difference().")
print("✔ Supports subset and superset operations.")
print("✔ Does not support add(), remove(), pop(), or clear().")
print("✔ Can be used as a dictionary key.")
print("✔ Useful for constant collections of data.")

print("=" * 65)
print("End of frozenset.py")
print("=" * 65)
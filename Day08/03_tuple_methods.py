#              TUPLE METHODS IN PYTHON
print("=" * 60)
print("              PYTHON TUPLE METHODS")
print("=" * 60)

# CREATE A TUPLE
numbers = (10, 20, 30, 20, 40, 50, 20)

print("\nOriginal Tuple")
print(numbers)

# TUPLE METHODS
print("\nPython tuples have only TWO built-in methods.")

# 1. count()
print("\n1. count()")

print("Count of 20 :", numbers.count(20))
print("Count of 10 :", numbers.count(10))
print("Count of 50 :", numbers.count(50))
print("Count of 100:", numbers.count(100))

# 2. index()
print("\n2. index()")

print("Index of 10 :", numbers.index(10))
print("Index of 20 :", numbers.index(20))
print("Index of 30 :", numbers.index(30))
print("Index of 40 :", numbers.index(40))
print("Index of 50 :", numbers.index(50))

# index() with Start Position
print("\n3. index() with Start Position")

letters = ("A", "B", "C", "B", "D", "B", "E")

print(letters)

print("First B  :", letters.index("B"))
print("Second B :", letters.index("B", 2))
print("Third B  :", letters.index("B", 4))

# USING len()
print("\n4. len()")

print("Length :", len(numbers))

# USING max()
print("\n5. max()")

print("Maximum Value :", max(numbers))

# USING min()
print("\n6. min()")

print("Minimum Value :", min(numbers))

# USING sum()
print("\n7. sum()")

print("Sum :", sum(numbers))

# USING sorted()
print("\n8. sorted()")

sorted_numbers = sorted(numbers)

print("Sorted List :", sorted_numbers)
print("Type :", type(sorted_numbers))

# USING tuple()
print("\n9. Convert Back to Tuple")

sorted_tuple = tuple(sorted_numbers)

print(sorted_tuple)

# USING reversed()
print("\n10. reversed()")

reverse_tuple = tuple(reversed(numbers))

print(reverse_tuple)

# USING enumerate()
print("\n11. enumerate()")

for index, value in enumerate(numbers):
    print(index, "->", value)

# LOOPING THROUGH TUPLE
print("\n12. for Loop")

for value in numbers:
    print(value)

# MEMBERSHIP OPERATORS
print("\n13. Membership Operators")

print("20 in tuple     :", 20 in numbers)
print("100 in tuple    :", 100 in numbers)

print("20 not in tuple :", 20 not in numbers)
print("100 not in tuple:", 100 not in numbers)

# TUPLE CONCATENATION
print("\n14. Concatenation")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)

# TUPLE REPETITION
print("\n15. Repetition")

print(("Python",) * 5)

# IMMUTABILITY DEMO
print("\n16. Immutability")

colors = ("Red", "Green", "Blue")

print(colors)

print("""
# colors.append("Black")
# colors.remove("Red")
# colors[0] = "Yellow"

All the above operations will raise errors because
tuples are immutable.
""")

# REAL-LIFE EXAMPLES
print("\n17. Real-Life Examples")

days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

print("Days in Week :", len(days))

print("Index of Friday :", days.index("Friday"))

print("Sunday Count :", days.count("Sunday"))

# COMMON MISTAKES
print("\n18. Common Mistakes")

print("""
Mistake 1:
Trying to use append()

Wrong:
numbers.append(60)

--------------------------------

Mistake 2:
Trying to remove elements

Wrong:
numbers.remove(20)

--------------------------------

Mistake 3:
Trying to change a value

Wrong:
numbers[0] = 100

--------------------------------

Reason:
Tuples are immutable.
""")

# SUMMARY
print("\n" + "=" * 60)
print("             TUPLE METHODS SUMMARY")
print("=" * 60)

print("Tuple Methods:")
print("✓ count()")
print("✓ index()")

print("\nUseful Built-in Functions:")
print("✓ len()")
print("✓ max()")
print("✓ min()")
print("✓ sum()")
print("✓ sorted()")
print("✓ tuple()")
print("✓ reversed()")
print("✓ enumerate()")

print("\nImportant Points:")
print("✓ Tuples have only TWO built-in methods.")
print("✓ Tuples are immutable.")
print("✓ They are faster than lists.")
print("✓ Best for storing fixed data.")

print("=" * 60)
print("End of tuples_methods.py")
print("=" * 60)
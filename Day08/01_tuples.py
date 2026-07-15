#                 TUPLES IN PYTHON
print("=" * 60)
print("                PYTHON TUPLES")
print("=" * 60)

# WHAT IS A TUPLE?
print("\n1. Creating Tuples")

# Empty tuple
empty_tuple = ()

# Integer tuple
numbers = (10, 20, 30, 40, 50)

# String tuple
fruits = ("Apple", "Banana", "Mango")

# Mixed data types
student = (101, "Bhomdev", 92.5, True)

# Nested tuple
employee = (
    (101, "Rahul"),
    (102, "Aman"),
    (103, "Priya")
)

print("Empty Tuple :", empty_tuple)
print("Numbers     :", numbers)
print("Fruits      :", fruits)
print("Student     :", student)
print("Employees   :", employee)

# SINGLE ELEMENT TUPLE
print("\n2. Single Element Tuple")

single = (100,)
not_tuple = (100)

print("Single Tuple :", single)
print("Type :", type(single))

print("Without Comma :", not_tuple)
print("Type :", type(not_tuple))

# TUPLE WITH DIFFERENT DATA TYPES
print("\n3. Different Data Types")

data = (
    101,
    "Bhomdev",
    5.10,
    True,
    "Python"
)

print(data)

# USING tuple() CONSTRUCTOR
print("\n4. tuple() Constructor")

list_data = [1, 2, 3, 4, 5]

new_tuple = tuple(list_data)

print("List :", list_data)
print("Tuple:", new_tuple)

# PACKING
print("\n5. Tuple Packing")

person = "Bhomdev", 22, "Python Developer"

print(person)

# UNPACKING
print("\n6. Tuple Unpacking")

name, age, profession = person

print("Name       :", name)
print("Age        :", age)
print("Profession :", profession)

# LENGTH OF TUPLE
print("\n7. Length of Tuple")

print("Length of numbers tuple :", len(numbers))

# MEMBERSHIP OPERATOR
print("\n8. Membership Operator")

print("Apple" in fruits)
print("Orange" in fruits)

print("Python" in data)
print("Java" not in data)

# CONCATENATION
print("\n9. Tuple Concatenation")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)

# REPETITION
print("\n10. Tuple Repetition")

print(("Python",) * 5)

# LOOPING THROUGH TUPLE
print("\n11. Using for Loop")

for fruit in fruits:
    print(fruit)

print("\nUsing while Loop")

index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1

# NESTED TUPLES
print("\n12. Nested Tuples")

students = (
    (101, "Rahul", 90),
    (102, "Aman", 85),
    (103, "Bhomdev", 95)
)

for student in students:
    print(student)

# IMMUTABILITY DEMO
print("\n13. Tuple Immutability")

marks = (90, 85, 95)

print("Original Tuple :", marks)

# marks[0] = 100
# This will raise TypeError because tuples are immutable.

print("Tuples cannot be modified after creation.")

# REAL-LIFE EXAMPLES
print("\n14. Real-Life Examples")

rgb_color = (255, 0, 0)
gps_location = (30.7333, 76.7794)
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

print("RGB Color :", rgb_color)
print("GPS       :", gps_location)
print("Days      :", days)

# TYPE CHECKING
print("\n15. Type Checking")

print(type(numbers))
print(type(student))
print(type(empty_tuple))

# SUMMARY
print("\n" + "=" * 60)
print("               TUPLE SUMMARY")
print("=" * 60)

print("✓ Tuples are Ordered")
print("✓ Tuples are Immutable")
print("✓ Allow Duplicate Values")
print("✓ Support Indexing")
print("✓ Support Slicing")
print("✓ Can Store Multiple Data Types")
print("✓ Faster than Lists")
print("✓ Useful for Fixed Data")

print("=" * 60)
print("End of tuples.py")
print("=" * 60)
#              TUPLE INDEXING IN PYTHON
print("=" * 60)
print("              PYTHON TUPLE INDEXING")
print("=" * 60)

# CREATE A TUPLE
fruits = (
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    "Grapes",
    "Pineapple"
)

print("\nOriginal Tuple")
print(fruits)

# POSITIVE INDEXING
print("\n1. Positive Indexing")

print("Index 0 :", fruits[0])
print("Index 1 :", fruits[1])
print("Index 2 :", fruits[2])
print("Index 3 :", fruits[3])
print("Index 4 :", fruits[4])
print("Index 5 :", fruits[5])

# NEGATIVE INDEXING
print("\n2. Negative Indexing")

print("Index -1 :", fruits[-1])
print("Index -2 :", fruits[-2])
print("Index -3 :", fruits[-3])
print("Index -4 :", fruits[-4])
print("Index -5 :", fruits[-5])
print("Index -6 :", fruits[-6])

# INDEXING WITH DIFFERENT DATA TYPES
print("\n3. Mixed Data Type Tuple")

student = (
    101,
    "Bhomdev",
    22,
    5.10,
    True,
    "Python Developer"
)

print(student)

print("\nAccess Individual Values")

print("ID         :", student[0])
print("Name       :", student[1])
print("Age        :", student[2])
print("Height     :", student[3])
print("Student    :", student[4])
print("Profession :", student[5])

# NESTED TUPLE INDEXING
print("\n4. Nested Tuple Indexing")

employees = (
    (101, "Rahul", "Developer"),
    (102, "Aman", "Designer"),
    (103, "Bhomdev", "Python Developer")
)

print(employees)

print("\nAccess Nested Values")

print("First Employee      :", employees[0])
print("Second Employee     :", employees[1])
print("Third Employee      :", employees[2])

print("\nSpecific Values")

print("Employee ID         :", employees[0][0])
print("Employee Name       :", employees[0][1])

print("Employee ID         :", employees[1][0])
print("Employee Name       :", employees[1][1])

print("Employee Profession :", employees[2][2])

# USING VARIABLES AS INDEX
print("\n5. Using Variable as Index")

index = 3

print("Fruit at Index", index, ":", fruits[index])

# USING len()
print("\n6. Last Element Using len()")

last_index = len(fruits) - 1

print("Last Index :", last_index)
print("Last Fruit :", fruits[last_index])

# LOOP THROUGH TUPLE USING INDEX
print("\n7. Using for Loop with Index")

for i in range(len(fruits)):
    print(f"Index {i} -> {fruits[i]}")

# WHILE LOOP
print("\n8. Using while Loop")

i = 0

while i < len(fruits):
    print(f"Index {i} -> {fruits[i]}")
    i += 1

# IMMUTABILITY DEMO
print("\n9. Tuple is Immutable")

numbers = (10, 20, 30, 40)

print("Original Tuple :", numbers)

# numbers[1] = 100
# This line will raise TypeError because tuples are immutable.

print("You cannot modify tuple elements.")

# INDEX ERROR DEMO
print("\n10. Index Error Example")

print("Tuple Length :", len(fruits))

print("""
# fruits[10]

This will raise:

IndexError: tuple index out of range
""")

# REAL-LIFE EXAMPLE
print("\n11. Real-Life Example")

student = (
    101,
    "Bhomdev",
    "Python Developer",
    "India"
)

print(f"Student ID   : {student[0]}")
print(f"Name         : {student[1]}")
print(f"Profession   : {student[2]}")
print(f"Country      : {student[3]}")

# SUMMARY
print("\n" + "=" * 60)
print("           TUPLE INDEXING SUMMARY")
print("=" * 60)

print("✓ Positive Index Starts from 0")
print("✓ Negative Index Starts from -1")
print("✓ Nested Tuples Support Multiple Indexes")
print("✓ Tuples Support Indexing Like Lists")
print("✓ Tuples are Immutable")
print("✓ Invalid Index Raises IndexError")

print("=" * 60)
print("End of tuples_indexing.py")
print("=" * 60)
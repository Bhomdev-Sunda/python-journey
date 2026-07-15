#         TUPLE PACKING & UNPACKING IN PYTHON
print("=" * 60)
print("       PYTHON TUPLE PACKING & UNPACKING")
print("=" * 60)

# WHAT IS TUPLE PACKING?
print("\n1. Tuple Packing")

student = "Bhomdev", 22, "Python Developer", True

print("Packed Tuple :", student)
print("Type         :", type(student))

# EXAMPLE 2
print("\n2. Employee Record")

employee = 101, "Rahul", "Developer", 50000

print(employee)

# EXAMPLE 3
print("\n3. RGB Color")

rgb = 255, 128, 0

print(rgb)

# WHAT IS UNPACKING?
print("\n4. Tuple Unpacking")

name, age, profession, is_student = student

print("Name        :", name)
print("Age         :", age)
print("Profession  :", profession)
print("Student     :", is_student)

# ANOTHER EXAMPLE
print("\n5. Employee Unpacking")

emp_id, emp_name, emp_job, salary = employee

print("Employee ID :", emp_id)
print("Name        :", emp_name)
print("Job         :", emp_job)
print("Salary      :", salary)

# SWAPPING VARIABLES
print("\n6. Swapping Variables")

a = 10
b = 20

print("Before Swapping")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter Swapping")
print("a =", a)
print("b =", b)

# MULTIPLE ASSIGNMENT
print("\n7. Multiple Assignment")

x, y, z = 100, 200, 300

print("x =", x)
print("y =", y)
print("z =", z)

# USING ASTERISK (*)
print("\n8. Unpacking with *")

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First  :", first)
print("Middle :", middle)
print("Last   :", last)

# ANOTHER ASTERISK EXAMPLE
print("\n9. Another * Example")

first, *remaining = numbers

print("First      :", first)
print("Remaining  :", remaining)

# IGNORING VALUES
print("\n10. Ignoring Values")

student = ("Bhomdev", 22, "Python", "India")

name, _, course, _ = student

print("Name   :", name)
print("Course :", course)

# NESTED TUPLE UNPACKING
print("\n11. Nested Tuple Unpacking")

employee = (
    101,
    "Bhomdev",
    ("Python", "AI", "SQL")
)

emp_id, emp_name, skills = employee

print("ID      :", emp_id)
print("Name    :", emp_name)
print("Skills  :", skills)

skill1, skill2, skill3 = skills

print("Skill 1 :", skill1)
print("Skill 2 :", skill2)
print("Skill 3 :", skill3)

# LOOP UNPACKING
print("\n12. Loop Unpacking")

students = (
    (101, "Rahul", 90),
    (102, "Aman", 85),
    (103, "Bhomdev", 95)
)

for roll, name, marks in students:
    print(f"Roll: {roll} | Name: {name} | Marks: {marks}")

# RETURNING MULTIPLE VALUES
print("\n13. Returning Multiple Values")

# (Functions will be covered later.
# This example is only for understanding.)

result = (500, 450, 50)

total, obtained, remaining = result

print("Total     :", total)
print("Obtained  :", obtained)
print("Remaining :", remaining)

# COMMON MISTAKES
print("\n14. Common Mistakes")

print("""
Mistake 1:
name, age = ("Bhomdev", 22, "Python")

Error:
ValueError
Too many values to unpack

----------------------------------------

Mistake 2:
name, age, course = ("Bhomdev", 22)

Error:
ValueError
Not enough values to unpack

----------------------------------------

Always keep the number of variables
equal to the number of values,
unless using *.
""")

# REAL-LIFE EXAMPLES
print("\n15. Real-Life Examples")

location = (30.7333, 76.7794)

latitude, longitude = location

print("Latitude  :", latitude)
print("Longitude :", longitude)

rgb = (255, 255, 0)

red, green, blue = rgb

print("Red   :", red)
print("Green :", green)
print("Blue  :", blue)

# SUMMARY
print("\n" + "=" * 60)
print("      TUPLE PACKING & UNPACKING SUMMARY")
print("=" * 60)

print("✓ Packing combines values into one tuple.")
print("✓ Unpacking extracts tuple values into variables.")
print("✓ Swapping variables uses unpacking.")
print("✓ Multiple assignment uses tuple packing.")
print("✓ * collects multiple values.")
print("✓ _ can ignore unwanted values.")
print("✓ Nested tuples can also be unpacked.")
print("✓ Loop unpacking makes code cleaner.")
print("✓ Widely used in Python functions.")

print("=" * 60)
print("End of tuple_packing_unpacking.py")
print("=" * 60)
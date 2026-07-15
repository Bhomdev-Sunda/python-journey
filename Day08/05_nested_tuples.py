#                 NESTED TUPLES IN PYTHON
print("=" * 60)
print("               PYTHON NESTED TUPLES")
print("=" * 60)

# WHAT IS A NESTED TUPLE?
print("\n1. Creating Nested Tuples")

students = (
    (101, "Rahul", 90),
    (102, "Aman", 85),
    (103, "Bhomdev", 95),
    (104, "Priya", 88)
)

print(students)

# ACCESSING COMPLETE TUPLES
print("\n2. Accessing Complete Tuples")

print("First Student  :", students[0])
print("Second Student :", students[1])
print("Third Student  :", students[2])
print("Fourth Student :", students[3])

# ACCESSING INDIVIDUAL VALUES
print("\n3. Accessing Individual Values")

print("Student ID      :", students[0][0])
print("Student Name    :", students[0][1])
print("Student Marks   :", students[0][2])

print()

print("Student ID      :", students[2][0])
print("Student Name    :", students[2][1])
print("Student Marks   :", students[2][2])

# NEGATIVE INDEXING
print("\n4. Negative Indexing")

print("Last Student    :", students[-1])
print("Last Student ID :", students[-1][0])
print("Last Student Name :", students[-1][1])

# LOOP THROUGH NESTED TUPLES
print("\n5. Using for Loop")

for student in students:
    print(student)

# LOOP UNPACKING
print("\n6. Loop Unpacking")

for roll, name, marks in students:
    print(f"Roll: {roll} | Name: {name} | Marks: {marks}")

# CALCULATE TOTAL MARKS
print("\n7. Total Marks")

total_marks = 0

for student in students:
    total_marks += student[2]

print("Total Marks :", total_marks)

# CALCULATE AVERAGE
print("\n8. Average Marks")

average = total_marks / len(students)

print(f"Average Marks : {average:.2f}")

# FIND TOPPER
print("\n9. Finding Topper")

highest_marks = 0
topper = ""

for student in students:

    if student[2] > highest_marks:

        highest_marks = student[2]
        topper = student[1]

print("Topper :", topper)
print("Marks  :", highest_marks)

# NESTED TUPLE OF EMPLOYEES
print("\n10. Employee Records")

employees = (
    (101, "Rahul", "Developer", 50000),
    (102, "Aman", "Designer", 45000),
    (103, "Bhomdev", "Python Developer", 70000)
)

for emp_id, name, job, salary in employees:

    print("-" * 50)

    print("Employee ID :", emp_id)
    print("Name        :", name)
    print("Job         :", job)
    print("Salary      :", salary)

# NESTED TUPLE OF PRODUCTS
print("\n11. Product Inventory")

products = (
    (101, "Laptop", 65000),
    (102, "Keyboard", 1200),
    (103, "Mouse", 700),
    (104, "Monitor", 15000)
)

for product in products:
    print(product)

# SEARCH A PRODUCT
print("\n12. Search Product")

search = input("Enter Product Name : ").title()

found = False

for product in products:

    if product[1] == search:

        print("\nProduct Found")
        print("ID    :", product[0])
        print("Name  :", product[1])
        print("Price :", product[2])

        found = True
        break

if not found:
    print("Product Not Found")

# MEMBERSHIP OPERATOR
print("\n13. Membership Operator")

days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
)

print("Monday" in days)
print("Sunday" in days)

# NESTED TUPLE WITH DIFFERENT DATA TYPES
print("\n14. Mixed Nested Tuple")

company = (
    (101, "Rahul", True),
    (102, "Aman", False),
    (103, "Bhomdev", True)
)

for emp_id, name, active in company:

    print(f"{emp_id} | {name} | Active: {active}")

# IMMUTABILITY DEMO
print("\n15. Tuple Immutability")

print("""
students[0][1] = "Rohan"

This will raise:

TypeError

Reason:
Tuples are immutable.
""")

# REAL-LIFE APPLICATIONS
print("\n16. Real-Life Applications")

gps_locations = (
    ("Delhi", 28.7041, 77.1025),
    ("Mumbai", 19.0760, 72.8777),
    ("Chandigarh", 30.7333, 76.7794)
)

for city, latitude, longitude in gps_locations:

    print(f"{city} -> ({latitude}, {longitude})")

# SUMMARY
print("\n" + "=" * 60)
print("            NESTED TUPLES SUMMARY")
print("=" * 60)

print("✓ Tuple inside another tuple is called a Nested Tuple.")
print("✓ Access nested values using multiple indexes.")
print("✓ Supports positive and negative indexing.")
print("✓ Works with for and while loops.")
print("✓ Loop unpacking makes code cleaner.")
print("✓ Commonly used for structured records.")
print("✓ Tuples are immutable.")
print("✓ Useful for student, employee, product, and GPS records.")

print("=" * 60)
print("End of nested_tuples.py")
print("=" * 60)
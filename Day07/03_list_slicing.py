#               LIST SLICING IN PYTHON
print("=" * 60)
print("         EMPLOYEE MANAGEMENT SYSTEM")
print("=" * 60)

# Employee List
employees = [
    "Bhomdev",
    "Rahul",
    "Priya",
    "Aman",
    "Neha",
    "Rohit",
    "Simran",
    "Karan",
    "Anjali",
    "Vikas"
]

# Display Complete List
print("\nAll Employees")
print(employees)

# List Slicing
print("\nFirst 3 Employees")
print(employees[:3])

print("\nLast 3 Employees")
print(employees[-3:])

print("\nEmployees from Index 2 to 5")
print(employees[2:6])

print("\nEmployees from Index 4 to End")
print(employees[4:])

print("\nEmployees from Start to Index 5")
print(employees[:6])

print("\nEvery 2nd Employee")
print(employees[::2])

print("\nEvery 3rd Employee")
print(employees[::3])

print("\nReverse Employee List")
print(employees[::-1])

print("\nReverse Every 2nd Employee")
print(employees[::-2])

print("\nCopy of Employee List")
print(employees[:])

# List Information
print("\nTotal Employees :", len(employees))

# End
print("\n" + "=" * 60)
print("Employee List Slicing Completed Successfully.")
print("=" * 60)
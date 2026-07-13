#               LIST INDEXING IN PYTHON
print("=" * 60)
print("          EMPLOYEE MANAGEMENT SYSTEM")
print("=" * 60)

# Employee List
employees = [
    "Bhomdev",
    "Rahul",
    "Priya",
    "Aman",
    "Neha"
]

# Display Complete List
print("\nEmployee List")
print(employees)

# Positive Indexing
print("\nPositive Indexing")

print(f"First Employee   : {employees[0]}")
print(f"Second Employee  : {employees[1]}")
print(f"Third Employee   : {employees[2]}")
print(f"Fourth Employee  : {employees[3]}")
print(f"Fifth Employee   : {employees[4]}")

# Negative Indexing
print("\nNegative Indexing")

print(f"Last Employee        : {employees[-1]}")
print(f"Second Last Employee : {employees[-2]}")
print(f"Third Last Employee  : {employees[-3]}")
print(f"Fourth Last Employee : {employees[-4]}")
print(f"First Employee       : {employees[-5]}")

# Using Index Values in Output
print("\nEmployee Details")

print(f"Employee ID 101 : {employees[0]}")
print(f"Employee ID 102 : {employees[1]}")
print(f"Employee ID 103 : {employees[2]}")
print(f"Employee ID 104 : {employees[3]}")
print(f"Employee ID 105 : {employees[4]}")

# List Information
print("\nTotal Employees :", len(employees))

# End
print("\n" + "=" * 60)
print("Employee Records Accessed Successfully.")
print("=" * 60)
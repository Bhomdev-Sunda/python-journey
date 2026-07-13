#               NESTED LISTS IN PYTHON
print("=" * 60)
print("         EMPLOYEE MANAGEMENT SYSTEM")
print("=" * 60)

# Nested List
employees = [
    [101, "Bhomdev", "Python Developer", 45000],
    [102, "Rahul", "Frontend Developer", 40000],
    [103, "Priya", "UI/UX Designer", 42000],
    [104, "Aman", "Data Analyst", 48000],
    [105, "Neha", "HR Manager", 50000]
]

# Display Complete Nested List
print("\nComplete Employee Database\n")
print(employees)

# Access Entire Records
print("\n" + "-" * 60)
print("ACCESSING COMPLETE RECORDS")
print("-" * 60)

print(f"Employee 1 : {employees[0]}")
print(f"Employee 2 : {employees[1]}")
print(f"Employee 3 : {employees[2]}")
print(f"Employee 4 : {employees[3]}")
print(f"Employee 5 : {employees[4]}")

# Access Individual Elements
print("\n" + "-" * 60)
print("ACCESSING INDIVIDUAL ELEMENTS")
print("-" * 60)

print(f"First Employee Name      : {employees[0][1]}")
print(f"Second Employee ID       : {employees[1][0]}")
print(f"Third Employee Position  : {employees[2][2]}")
print(f"Fourth Employee Salary   : ₹{employees[3][3]}")
print(f"Fifth Employee Name      : {employees[4][1]}")

# Display Employee Report
print("\n" + "-" * 60)
print("EMPLOYEE REPORT")
print("-" * 60)

for employee in employees:
    print(f"""
Employee ID     : {employee[0]}
Employee Name   : {employee[1]}
Designation     : {employee[2]}
Salary          : ₹{employee[3]}
------------------------------------------------------------
""")

# Nested Loop Example
print("-" * 60)
print("DISPLAYING ALL VALUES USING NESTED LOOPS")
print("-" * 60)

for employee in employees:
    for detail in employee:
        print(detail, end=" | ")
    print()

# List Information
print("\nTotal Employees :", len(employees))

# End
print("\n" + "=" * 60)
print("Employee Database Loaded Successfully.")
print("=" * 60)
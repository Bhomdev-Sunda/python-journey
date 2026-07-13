#                  LISTS IN PYTHON
print("=" * 60)
print("           COMPANY EMPLOYEE MANAGEMENT")
print("=" * 60)

employee_names = [
    "Bhomdev",
    "Rahul",
    "Priya",
    "Aman",
    "Neha"
]

employee_ids = [
    101,
    102,
    103,
    104,
    105
]

employee_salaries = [
    35000,
    42000,
    38000,
    45000,
    40000
]

employee_status = [
    True,
    True,
    False,
    True,
    True
]

# Mixed Data Type List
employee_details = [
    "Bhomdev",
    101,
    "Python Developer",
    35000,
    True
]

# Empty List
new_employees = []

# Display Lists
print("\nEmployee Names")
print(employee_names)

print("\nEmployee IDs")
print(employee_ids)

print("\nEmployee Salaries")
print(employee_salaries)

print("\nEmployee Status")
print(employee_status)

print("\nEmployee Details")
print(employee_details)

print("\nNew Employees")
print(new_employees)

# Display Data Type
print("\nData Types")

print(f"employee_names      : {type(employee_names)}")
print(f"employee_ids        : {type(employee_ids)}")
print(f"employee_salaries   : {type(employee_salaries)}")
print(f"employee_status     : {type(employee_status)}")
print(f"employee_details    : {type(employee_details)}")
print(f"new_employees       : {type(new_employees)}")

# List Information
print("\nTotal Employees :", len(employee_names))
print("Total Employee IDs :", len(employee_ids))
print("Total Salaries Stored :", len(employee_salaries))

# End
print("\n" + "=" * 60)
print("Employee Records Loaded Successfully.")
print("=" * 60)
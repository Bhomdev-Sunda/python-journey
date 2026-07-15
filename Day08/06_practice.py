#          COMPANY EMPLOYEE DIRECTORY SYSTEM
print("=" * 60)
print("      COMPANY EMPLOYEE DIRECTORY SYSTEM")
print("=" * 60)

# EMPLOYEE DATABASE (Nested Tuples)
# (ID, Name, Department, Salary)
employees = (
    (101, "Rahul", "HR", 35000),
    (102, "Aman", "Sales", 42000),
    (103, "Bhomdev", "IT", 55000),
    (104, "Priya", "Finance", 48000),
    (105, "Neha", "IT", 60000)
)

# DISPLAY ALL EMPLOYEES
print("\nEmployee List")
print("-" * 60)

for employee in employees:

    emp_id, name, department, salary = employee

    print(f"""
Employee ID : {emp_id}
Name        : {name}
Department  : {department}
Salary      : ₹{salary}
""")

# SEARCH EMPLOYEE
print("=" * 60)

search_id = int(input("Enter Employee ID : "))

found = False

for employee in employees:

    emp_id, name, department, salary = employee

    if emp_id == search_id:

        print("\nEmployee Found")
        print("-" * 40)

        print(f"ID         : {emp_id}")
        print(f"Name       : {name}")
        print(f"Department : {department}")
        print(f"Salary     : ₹{salary}")

        found = True
        break

if not found:
    print("\nEmployee Not Found.")

# TUPLE METHODS
print("\n" + "=" * 60)
print("TUPLE METHODS")
print("=" * 60)

departments = (
    "HR",
    "Sales",
    "IT",
    "Finance",
    "IT",
    "HR",
    "IT"
)

print("Departments :", departments)

print("IT Count     :", departments.count("IT"))
print("HR Count     :", departments.count("HR"))
print("Sales Index  :", departments.index("Sales"))

# TUPLE PACKING
print("\n" + "=" * 60)
print("TUPLE PACKING")
print("=" * 60)

new_employee = 106, "Rohit", "Support", 38000

print("Packed Tuple")
print(new_employee)

# TUPLE UNPACKING
print("\n" + "=" * 60)
print("TUPLE UNPACKING")
print("=" * 60)

emp_id, name, department, salary = new_employee

print("Employee ID :", emp_id)
print("Name        :", name)
print("Department  :", department)
print("Salary      :", salary)

# INDEXING
print("\n" + "=" * 60)
print("TUPLE INDEXING")
print("=" * 60)

print("First Employee :", employees[0])
print("Last Employee  :", employees[-1])

print("\nAccess Individual Values")

print("First Employee Name :", employees[0][1])
print("Third Employee Dept :", employees[2][2])
print("Last Salary         :", employees[-1][3])

# FIND HIGHEST SALARY
print("\n" + "=" * 60)
print("HIGHEST SALARY")
print("=" * 60)

highest_salary = employees[0][3]
highest_employee = employees[0]

for employee in employees:

    if employee[3] > highest_salary:

        highest_salary = employee[3]
        highest_employee = employee

emp_id, name, department, salary = highest_employee

print(f"""
Employee ID : {emp_id}
Name        : {name}
Department  : {department}
Salary      : ₹{salary}
""")

# DISPLAY ALL DEPARTMENTS
print("=" * 60)
print("DEPARTMENTS")
print("=" * 60)

for department in departments:
    print(department)

# SUMMARY
print("\n" + "=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

print("Total Employees :", len(employees))
print("Highest Salary  : ₹", highest_salary)
print("IT Employees    :", departments.count("IT"))
print("HR Employees    :", departments.count("HR"))

print("=" * 60)
print("End of Practice Project")
print("=" * 60)